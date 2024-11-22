import os
from collections import defaultdict
from typing import List, Dict


class MemoryLogger:
    """Class for logging memory usage."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MemoryLogger, cls).__new__(cls)
            cls._instance.max_memory = 0
        return cls._instance

    def reset(self):
        self.max_memory = 0

    def check_memory(self):
        import psutil

        process = psutil.Process(os.getpid())
        current_memory = process.memory_info().rss / (1024**2)  # Memory in MB
        self.max_memory = max(self.max_memory, current_memory)
        return current_memory


class AlgoTKUCEP:
    """Implementation of the TKU-CEP algorithm."""

    def __init__(self):
        self.K = 0  # Top-k HUIs
        self.transaction_count = 0
        self.CUV = 0  # Critical Utility Value
        self.map_item_to_u = {}  # Maps items to utilities
        self.map_item_to_twu = {}  # Maps items to Transaction-Weighted Utility (TWU)
        self.database = []  # Filtered database of transactions
        self.twu_pattern = []  # Items with TWU above CUV
        self.hui_sets = []  # List of high-utility itemsets

    def run_algorithm(self, input_file: str, output_file: str, top_k: int):
        """Run the algorithm to find top-k HUIs."""
        self.K = top_k
        MemoryLogger().reset()
        self._first_scan(input_file)
        self._calculate_cuv()
        self._filter_promising_items()
        self._second_scan(input_file)
        self._process_huis(output_file)

    def _first_scan(self, input_file: str):
        """First database scan to calculate TWU and utility for each item."""
        with open(input_file, "r") as file:
            for line in file:
                if not line.strip() or line.startswith(("#", "%", "@")):
                    continue
                self.transaction_count += 1
                items, transaction_utility, utilities = line.strip().split(":")
                items = list(map(int, items.split()))
                utilities = list(map(int, utilities.split()))
                transaction_utility = int(transaction_utility)
                for item, utility in zip(items, utilities):
                    self.map_item_to_u[item] = self.map_item_to_u.get(item, 0) + utility
                    self.map_item_to_twu[item] = (
                        self.map_item_to_twu.get(item, 0) + transaction_utility
                    )

    def _calculate_cuv(self):
        """Calculate the critical utility value (CUV) for top-k filtering."""
        sorted_utilities = sorted(self.map_item_to_u.values(), reverse=True)
        if len(sorted_utilities) >= self.K:
            self.CUV = sorted_utilities[self.K - 1]
        print(f"Critical Utility Value (CUV): {self.CUV}")

    def _filter_promising_items(self):
        """Filter items with TWU >= CUV."""
        self.twu_pattern = [
            item for item, twu in self.map_item_to_twu.items() if twu >= self.CUV
        ]
        print(f"Promising items: {self.twu_pattern}")

    def _second_scan(self, input_file: str):
        """Second database scan to filter transactions based on promising items."""
        with open(input_file, "r") as file:
            for line in file:
                if not line.strip() or line.startswith(("#", "%", "@")):
                    continue
                items, _, utilities = line.strip().split(":")
                items = list(map(int, items.split()))
                utilities = list(map(int, utilities.split()))
                revised_transaction = [
                    {"item": item, "utility": utility}
                    for item, utility in zip(items, utilities)
                    if item in self.twu_pattern
                ]
                if revised_transaction:
                    self.database.append(revised_transaction)
        print(f"Filtered database: {self.database}")

    def _process_huis(self, output_file: str):
        """Process top-k high-utility itemsets and write them to the output file."""
        for transaction in self.database:
            itemset = [entry["item"] for entry in transaction]
            utility = sum(entry["utility"] for entry in transaction)
            if len(self.hui_sets) < self.K or utility > self.hui_sets[-1]["fitness"]:
                self.hui_sets.append({"itemset": itemset, "fitness": utility})
                self.hui_sets = sorted(
                    self.hui_sets, key=lambda x: x["fitness"], reverse=True
                )[: self.K]

        with open(output_file, "w") as writer:
            for hui in self.hui_sets:
                writer.write(
                    f"{' '.join(map(str, hui['itemset']))} #UTIL:{hui['fitness']}\n"
                )
        print(f"High-utility itemsets written to {output_file}")

    def print_stats(self):
        """Print statistics about the algorithm's execution."""
        print("============ TKU-CEP Algorithm Stats ============")
        print(f"Transactions processed: {self.transaction_count}")
        print(f"Top-k HUIs: {len(self.hui_sets)}")
        print(f"Max memory usage: {MemoryLogger().max_memory:.2f} MB")
        print("=================================================")


# Example usage
if __name__ == "__main__":

    input_file = "DB_Utility.txt"
    output_file = "output.txt"

    # Run the algorithm
    top_k = 3
    algo = AlgoTKUCEP()
    algo.run_algorithm(input_file, output_file, top_k)
    algo.print_stats()

    # Print the results
    with open(output_file, "r") as f:
        print(f.read())
