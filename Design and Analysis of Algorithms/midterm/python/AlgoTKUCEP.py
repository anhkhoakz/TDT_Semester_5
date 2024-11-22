import time
from MemoryLogger import MemoryLogger


class AlgoTKUCEP:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.max_memory = 0
        self.transaction_count = 0
        self.database = []
        self.top_k_huis = []
        self.map_item_to_twu = {}
        self.map_item_to_u = {}
        self.twu_pattern = []
        self.CUV = 0
        self.K = 0
        self.samples = []
        self.p = []

    def run_algorithm(self, input_file, output_file, top_k):
        self.start_time = time.time()
        MemoryLogger.get_instance().reset()

        self.K = top_k
        self._process_input(input_file)
        self._calculate_CUV()

        self._filter_twu_pattern()
        self._construct_database(input_file)

        self._mine_top_k_huis()
        self._write_output(output_file)

        self.end_time = time.time()
        self.max_memory = MemoryLogger.get_instance().get_max_memory()

    def _process_input(self, input_file):
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
                parts = line.split(":")
                items = list(map(int, parts[0].strip().split(" ")))
                utilities = list(map(int, parts[2].strip().split(" ")))
                transaction_utility = int(parts[1])

                for item, utility in zip(items, utilities):
                    self.map_item_to_u[item] = self.map_item_to_u.get(item, 0) + utility
                    self.map_item_to_twu[item] = (
                        self.map_item_to_twu.get(item, 0) + transaction_utility
                    )

    def _calculate_CUV(self):
        utilities = sorted(self.map_item_to_u.values(), reverse=True)
        if len(utilities) >= self.K:
            self.CUV = utilities[self.K - 1]
        else:
            self.CUV = utilities[-1] if utilities else 0

    def _filter_twu_pattern(self):
        self.twu_pattern = [
            item for item, twu in self.map_item_to_twu.items() if twu >= self.CUV
        ]

    def _construct_database(self, input_file):
        with open(input_file, "r") as file:
            for line in file:
                if (
                    line.startswith("#")
                    or line.startswith("%")
                    or line.startswith("@")
                    or not line.strip()
                ):
                    continue

                parts = line.split(":")
                items = list(map(int, parts[0].strip().split(" ")))
                utilities = list(map(int, parts[2].strip().split(" ")))

                transaction = [
                    {"item": item, "utility": utility}
                    for item, utility in zip(items, utilities)
                    if item in self.twu_pattern
                ]
                if transaction:
                    self.database.append(transaction)

    def _mine_top_k_huis(self):
        # Implement the algorithm logic for finding Top-K HUIs
        pass

    def _write_output(self, output_file):
        with open(output_file, "w") as writer:
            for hui in self.top_k_huis:
                writer.write(f"{hui}\n")

    def print_stats(self):
        print(f"============ TKU-CE+ Algorithm ===========")
        print(f"Total time: {self.end_time - self.start_time:.2f} seconds")
        print(f"Max memory used: {self.max_memory:.2f} MB")
        print(f"Transaction count: {self.transaction_count}")
        print(f"High-Utility Itemsets: {len(self.top_k_huis)}")
        print(f"==========================================")
