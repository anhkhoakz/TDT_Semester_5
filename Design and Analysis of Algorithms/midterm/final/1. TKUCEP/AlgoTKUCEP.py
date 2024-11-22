from bitarray import bitarray
import random
import time
import os
import psutil


class MemoryLogger:
    def __init__(self):
        self.max_memory = 0

    def get_max_memory(self):
        """Get the maximum memory usage observed."""
        return self.max_memory

    def reset(self):
        """Reset the maximum memory usage tracker."""
        self.max_memory = 0

    def check_memory(self):
        """Check and update the current memory usage."""
        process = psutil.Process(os.getpid())
        current_memory = process.memory_info().rss / 1024 / 1024
        if current_memory > self.max_memory:
            self.max_memory = current_memory
        return current_memory


class Pair:
    def __init__(self, item=0, utility=0):
        """Constructor for the Pair class.

        Args:
            item (int, optional): The item. Defaults to 0.
            utility (int, optional): The utility. Defaults to 0.
        """
        self.item = item
        self.utility = utility


class Particle:
    def __init__(self, length=0):
        """Initialize a particle with a binary array and fitness value.

        Args:
            length (int, optional): The length of the binary array. Defaults to 0.
        """
        self.X = bitarray(length)
        self.X.setall(0)
        self.fitness = 0

    def copy_particle(self, particle):
        """Copy the content of another particle.

        Args:
            particle (_type_): The particle to copy.
        """
        self.X = particle.X.copy()
        self.fitness = particle.fitness

    def calculate_fitness(
        self,
        k: int,
        templist: list[int],
        database: list[list[Pair]],
        twu_pattern: list[int],
    ):
        """ "Calculate the fitness value of the particle

        Args:
            k (int): The number of selected items in the pattern.
            templist (list[int]): List of transaction IDs where the particle exists.
            database (list[list[Pair]]): The transactional database.
            twu_pattern (list[int]): The list of TWU (transactional weighted utility) patterns.
        """

        if k == 0:
            return
        fitness = 0
        for p in templist:
            i = 0
            q = 0
            temp = 0
            sum_utility = 0
            while q < len(database[p]) and i < len(twu_pattern):
                if self.X[i]:
                    for t in range(len(database[p])):
                        if database[p][t].item == twu_pattern[i]:
                            sum_utility += database[p][t].utility
                            i += 1
                            temp += 1
                            break
                else:
                    i += 1
            if temp == k:
                fitness += sum_utility
        self.fitness = fitness


class HUI:
    def __init__(self, itemset: str, fitness: float):
        """Constructor for the HUI class.

        Args:
            itemset (str): The itemset represented as a string.
            fitness (float): The utility score (fitness) of the itemset.
        """
        self.itemset = itemset
        self.fitness = fitness


class Item:
    def __init__(self, item: int, transaction_count: int) -> None:
        """Constructor for the Item class.

        Args:
            item (int): The identifier of the item.
            transaction_count (int): The number of transactions in the dataset.
        """
        self.item = item
        self.TIDS = bitarray(transaction_count)
        self.TIDS.setall(0)


class AlgoTKUCEP:
    def __init__(self):
        """Initialize the algorithm parameters and data structures."""
        self.max_memory = 0.0
        self.start_timestamp = 0
        self.end_timestamp = 0
        self.sample_size = 2000
        self.max_iteration = 2000
        self.actual_iterations = 0
        self.transaction_count = 0
        self.K = 0
        self.CUV = 0
        self.rho = 0.2
        self.SF = 0.2
        self.map_item_to_u = {}
        self.map_item_to_twu = {}
        self.twu_pattern = []
        self.writer = None
        self.p = []
        self.samples = []
        self.hui_sets = []
        self.database = []
        self.items = []
        self.top_k_hui_particle = []

    def run_algorithm(self, input_file: str, output_file: str, top_k: int) -> None:
        """Run the TKUCEP algorithm.

        Args:
            input_file (str): Path to the input transaction file.
            output_file (str): Path to the output file to store results.
            top_k (int): The number of top high utility itemsets to find.
        """
        MemoryLogger().reset()
        self.K = top_k
        self.start_timestamp = time.time()
        self.writer = open(output_file, "w")
        self.map_item_to_u = {}
        self.map_item_to_twu = {}

        with open(input_file, "r") as file:
            for line in file:
                if (
                    line.startswith("#")
                    or line.startswith("%")
                    or line.startswith("@")
                    or not line.strip()
                ):
                    continue
                self.transaction_count += 1
                split = line.strip().split(":")
                items = list(map(int, split[0].split()))
                transaction_utility = int(split[1])
                utilities = list(map(int, split[2].split()))
                for i, item in enumerate(items):
                    utility = utilities[i]
                    self.map_item_to_u[item] = self.map_item_to_u.get(item, 0) + utility
                    self.map_item_to_twu[item] = (
                        self.map_item_to_twu.get(item, 0) + transaction_utility
                    )

        self.calculate_cuv(self.map_item_to_u)

        self.twu_pattern = [
            item for item, twu in self.map_item_to_twu.items() if twu >= self.CUV
        ]
        self.p = [0.0] * len(self.twu_pattern)

        with open(input_file, "r") as file:
            for line in file:
                if (
                    line.startswith("#")
                    or line.startswith("%")
                    or line.startswith("@")
                    or not line.strip()
                ):
                    continue
                split = line.strip().split(":")
                items = list(map(int, split[0].split()))
                utilities = list(map(int, split[2].split()))
                revised_transaction = [
                    Pair(item, utility)
                    for item, utility in zip(items, utilities)
                    if self.map_item_to_twu.get(item, 0) >= self.CUV
                ]
                self.database.append(revised_transaction)

        self.items = [Item(item, self.transaction_count) for item in self.twu_pattern]

        for i, transaction in enumerate(self.database):
            for item in self.items:
                for pair in transaction:
                    if item.item == pair.item:
                        item.TIDS[i] = 1

        MemoryLogger().check_memory()

        if self.twu_pattern:
            self.generate_sample(1.0)
            for i in range(self.max_iteration):
                self.actual_iterations += 1
                self.samples.sort(key=lambda x: -x.fitness)
                max_min = (
                    self.samples[0].fitness
                    - self.samples[int(self.rho * self.sample_size) - 1].fitness
                )
                proportion = max_min / self.samples[0].fitness
                if max_min == 0:
                    break
                self.update((1 - self.SF) * proportion)

            self.end_timestamp = time.time()
            for i in range(self.K):
                if i < len(self.top_k_hui_particle):
                    self.insert(self.top_k_hui_particle[i])

        MemoryLogger().check_memory()
        self.max_memory = MemoryLogger().get_max_memory()
        self.end_timestamp = time.time()
        self.write_out()
        self.writer.close()

    def calculate_cuv(self, map_item_to_u: dict[int, int]) -> None:
        """Calculate the CUV value.

        Args:
            map_item_to_u (dict[int, int]): Mapping of items to their utilities.
        """
        if not map_item_to_u:
            return
        sorted_utilities = sorted(map_item_to_u.values(), reverse=True)
        self.CUV = sorted_utilities[min(len(sorted_utilities), self.K) - 1]

    def generate_sample(self, proportion: float) -> None:
        """Generate a sample.

        Args:
            proportion (float): The proportion of particles to generate.
        """
        for i in range(int(proportion * self.sample_size)):
            temp_particle = Particle(len(self.twu_pattern))
            k = random.randint(1, len(self.twu_pattern))
            for _ in range(k):
                temp_particle.X[random.randint(0, len(self.twu_pattern) - 1)] = 1
            trans_list = []
            self.is_rba_individual(temp_particle, trans_list)
            temp_particle.calculate_fitness(
                k, trans_list, self.database, self.twu_pattern
            )
            self.samples.append(temp_particle)
            self.insert_top_list(temp_particle)

    def update(self, proportion: float) -> None:
        """Update particles based on fitness and probability.

        Args:
            proportion (float): The proportion of particles to update.
        """
        num = [0] * len(self.twu_pattern)
        for i in range(int(self.rho * self.sample_size)):
            for j in range(len(self.twu_pattern)):
                if self.samples[i].X[j]:
                    num[j] += 1
        self.CUV = self.samples[int(self.rho * self.sample_size - 1)].fitness
        for i in range(len(self.twu_pattern)):
            self.p[i] = num[i] / (self.rho * self.sample_size)
        for i in range(int(proportion * self.sample_size)):
            temp_particle = Particle(len(self.twu_pattern))
            self.update_particle(temp_particle)
            trans_list = []
            if self.is_rba_individual(temp_particle, trans_list):
                k = temp_particle.X.count()
                temp_particle.calculate_fitness(
                    k, trans_list, self.database, self.twu_pattern
                )
                if temp_particle.fitness > self.CUV:
                    self.samples.append(temp_particle)
                    self.insert_top_list(temp_particle)
        self.generate_sample(self.SF)

    def update_particle(self, temp_particle: Particle) -> None:
        """Update the particle.

        Args:
            temp_particle (Particle): The particle to update.
        """
        for i in range(len(self.twu_pattern)):
            if random.random() < self.p[i]:
                temp_particle.X[i] = 1

    def insert_top_list(self, temp_particle: Particle) -> None:
        """Insert a particle into the sorted top-k list of high-utility itemsets.

        Args:
            temp_particle (Particle): The particle representing an itemset and its fitness value.
        """
        temp = Particle()
        temp.copy_particle(temp_particle)
        if not self.top_k_hui_particle:
            self.top_k_hui_particle.append(temp)
            return
        if len(self.top_k_hui_particle) < self.K:
            if temp.fitness < self.top_k_hui_particle[-1].fitness:
                self.top_k_hui_particle.append(temp)
                return
        else:
            if temp.fitness < self.top_k_hui_particle[-1].fitness:
                return
        max_idx = 0
        min_idx = len(self.top_k_hui_particle) - 1
        while max_idx <= min_idx:
            mid_idx = (max_idx + min_idx) // 2
            if temp.fitness > self.top_k_hui_particle[mid_idx].fitness:
                min_idx = mid_idx - 1
            elif temp.fitness < self.top_k_hui_particle[mid_idx].fitness:
                max_idx = mid_idx + 1
            else:
                break
        if temp.fitness > self.top_k_hui_particle[mid_idx].fitness:
            self.top_k_hui_particle.insert(mid_idx, temp)
        elif temp.fitness < self.top_k_hui_particle[mid_idx].fitness:
            self.top_k_hui_particle.insert(mid_idx + 1, temp)
        else:
            if temp not in self.top_k_hui_particle:
                while self.top_k_hui_particle[mid_idx].fitness == temp.fitness:
                    if self.top_k_hui_particle[mid_idx].X == temp.X:
                        return
                    mid_idx -= 1
                    if mid_idx == -1:
                        break
                while self.top_k_hui_particle[mid_idx].fitness == temp.fitness:
                    if self.top_k_hui_particle[mid_idx].X == temp.X:
                        return
                    mid_idx += 1
                    if mid_idx == len(self.top_k_hui_particle):
                        break
                self.top_k_hui_particle.insert(mid_idx, temp)

    def is_rba_individual(self, temp_particle: Particle, temp_list: list[int]) -> bool:
        """Check if a particle is a valid Redundant-Bit Avoidance (RBA) individual.

        Args:
            temp_particle (Particle): The particle being checked.
            temp_list (list[int]): List to store transaction indices where the pattern exists.

        Returns:
            bool: True if the particle is an RBA individual, False otherwise.
        """
        templist = [i for i in range(len(self.twu_pattern)) if temp_particle.X[i]]
        if not templist:
            return False
        temp_bitset = self.items[templist[0]].TIDS.copy()
        mid_bitset = temp_bitset.copy()
        for i in range(1, len(templist)):
            temp_bitset &= self.items[templist[i]].TIDS
            if temp_bitset.count() != 0:
                mid_bitset = temp_bitset.copy()
            else:
                temp_bitset = mid_bitset.copy()
                temp_particle.X[templist[i]] = 0
        if temp_bitset.count() == 0:
            return False
        else:
            for m in range(len(temp_bitset)):
                if temp_bitset[m]:
                    temp_list.append(m)
            return True

    def insert(self, temp_particle: Particle) -> None:
        """Insert a particle into the list of high-utility itemsets if it is unique.

        Args:
            temp_particle (Particle): The particle representing an itemset.
        """
        temp = " ".join(
            str(self.twu_pattern[i])
            for i in range(len(self.twu_pattern))
            if temp_particle.X[i]
        )
        if not self.hui_sets:
            self.hui_sets.append(HUI(temp, temp_particle.fitness))
        else:
            for hui in self.hui_sets:
                if temp == hui.itemset:
                    break
            else:
                self.hui_sets.append(HUI(temp, temp_particle.fitness))

    def write_out(self):
        for hui in self.hui_sets:
            self.writer.write(f"{hui.itemset} #UTIL:{hui.fitness}\n")

    def print_stats(self):
        print("============ TKU-CE+ Algorithm ===========")
        print(f" Total time: {self.end_timestamp - self.start_timestamp} ms")
        print(f" Memory: {self.max_memory} MB")
        print(f" Actual iterations: {self.actual_iterations}")
        print(f" High-utility itemsets count: {len(self.hui_sets)}")
        print("==========================================")
