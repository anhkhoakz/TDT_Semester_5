"""
Document: 1-s2.0-S0020025522015882-main.pdf

Title: Efficient mining of top-k high utility itemsets through genetic algorithms
"""

from typing import List, Dict, Set, Tuple


def calculate_transaction_utility(
    transaction: Dict[int, int], external_utilities: Dict[int, int]
) -> int:
    """
    Calculates the transaction utility of a given transaction.

    Args:
        transaction: A dictionary representing a transaction with item keys and internal utility values.
        external_utilities: A dictionary with item keys and external utility values.

    Returns:
        int: The transaction utility value.
    """
    try:
        return sum(
            quantity * external_utilities[item]
            for item, quantity in transaction.items()
        )
    except KeyError as e:
        print(f"Error: Item {e} not found in external utilities.")
        return 0


def calculate_itemset_utility(
    itemset: Set[int],
    vertical_data: Dict[int, List[int]],
    horizontal_data: Dict[int, Dict[int, int]],
) -> int:
    """
    Calculates the utility of an itemset across all transactions.

    Args:
        itemset: A set of items representing the itemset.
        vertical_data: A dictionary for vertical data representation.
        horizontal_data: A dictionary for horizontal data representation.

    Returns:
        int: The utility value of the itemset.
    """
    try:
        transaction_indices = set.intersection(
            *[set(vertical_data[item]) for item in itemset]
        )
        return sum(
            sum(horizontal_data[tid][item] for item in itemset)
            for tid in transaction_indices
        )
    except KeyError as e:
        print(f"Error: Item or transaction {e} not found in data.")
        return 0


def deterministic_crossover(
    parent1: Set[int],
    parent2: Set[int],
    vertical_data: Dict[int, List[int]],
    horizontal_data: Dict[int, Dict[int, int]],
) -> Tuple[Set[int], Set[int]]:
    """
    Performs crossover between two parent itemsets deterministically.

    Args:
        parent1: The first parent itemset.
        parent2: The second parent itemset.
        vertical_data: A dictionary for vertical data representation.
        horizontal_data: A dictionary for horizontal data representation.

    Returns:
        Tuple[Set[int], Set[int]]: Two new offspring itemsets.
    """
    try:
        utility1 = calculate_itemset_utility(parent1, vertical_data, horizontal_data)
        utility2 = calculate_itemset_utility(parent2, vertical_data, horizontal_data)

        offspring1, offspring2 = parent1.copy(), parent2.copy()

        if utility1 > utility2:
            low_utility_item = min(
                parent1,
                key=lambda x: sum(horizontal_data[tid][x] for tid in vertical_data[x]),
            )
            high_utility_item = max(
                parent2,
                key=lambda x: sum(horizontal_data[tid][x] for tid in vertical_data[x]),
            )
            offspring1.remove(low_utility_item)
            offspring1.add(high_utility_item)
            offspring2.remove(high_utility_item)
            offspring2.add(low_utility_item)
        else:
            low_utility_item = min(
                parent2,
                key=lambda x: sum(horizontal_data[tid][x] for tid in vertical_data[x]),
            )
            high_utility_item = max(
                parent1,
                key=lambda x: sum(horizontal_data[tid][x] for tid in vertical_data[x]),
            )
            offspring2.remove(low_utility_item)
            offspring2.add(high_utility_item)
            offspring1.remove(high_utility_item)
            offspring1.add(low_utility_item)

        return offspring1, offspring2
    except KeyError as e:
        print(f"Error: Item or transaction {e} not found in data.")
        return parent1, parent2


def deterministic_mutation(
    itemset: Set[int],
    all_items: Set[int],
    vertical_data: Dict[int, List[int]],
    horizontal_data: Dict[int, Dict[int, int]],
) -> Set[int]:
    """
    Applies mutation on an itemset deterministically.

    Args:
        itemset: The itemset to mutate.
        all_items: A set of all items in the dataset.
        vertical_data: A dictionary for vertical data representation.
        horizontal_data: A dictionary for horizontal data representation.

    Returns:
        Set[int]: The mutated itemset.
    """
    try:
        if len(itemset) > 1:
            low_utility_item = min(
                itemset,
                key=lambda x: sum(horizontal_data[tid][x] for tid in vertical_data[x]),
            )
            itemset.remove(low_utility_item)
        else:
            remaining_items = all_items - itemset
            high_utility_item = max(
                remaining_items,
                key=lambda x: sum(horizontal_data[tid][x] for tid in vertical_data[x]),
            )
            itemset.add(high_utility_item)

        return itemset
    except KeyError as e:
        print(f"Error: Item or transaction {e} not found in data.")
        return itemset


def tkhuim_ga(
    vertical_data: Dict[int, List[int]],
    horizontal_data: Dict[int, Dict[int, int]],
    external_utilities: Dict[int, int],
    k: int,
    max_length: int,
) -> List[Set[int]]:
    """
    The TKHUIM-GA algorithm for mining top-k high utility itemsets deterministically.

    Args:
        vertical_data: A dictionary for vertical data representation.
        horizontal_data: A dictionary for horizontal data representation.
        external_utilities: A dictionary with item keys and external utility values.
        k: The desired number of top itemsets.
        max_length: The maximum length of an itemset.

    Returns:
        List[Set[int]]: A list of the top-k high utility itemsets.
    """
    try:
        all_items = set(vertical_data.keys())
        elite_population = [
            set([item])
            for item in sorted(
                all_items, key=lambda x: external_utilities[x], reverse=True
            )[:k]
        ]

        transactions = sorted(
            horizontal_data.keys(),
            key=lambda tid: calculate_transaction_utility(
                horizontal_data[tid], external_utilities
            ),
            reverse=True,
        )
        initial_population = []
        for tid in transactions[:k]:
            sorted_items = sorted(
                horizontal_data[tid].keys(),
                key=lambda x: horizontal_data[tid][x],
                reverse=True,
            )
            initial_population.append(set(sorted_items[:max_length]))

        generations_without_improvement = 0
        max_generations_without_improvement = 10

        while generations_without_improvement < max_generations_without_improvement:
            new_population = []
            for i in range(0, len(initial_population), 2):
                parent1, parent2 = (
                    initial_population[i],
                    initial_population[(i + 1) % len(initial_population)],
                )
                offspring1, offspring2 = deterministic_crossover(
                    parent1, parent2, vertical_data, horizontal_data
                )
                new_population.append(
                    deterministic_mutation(
                        offspring1, all_items, vertical_data, horizontal_data
                    )
                )
                new_population.append(
                    deterministic_mutation(
                        offspring2, all_items, vertical_data, horizontal_data
                    )
                )

            new_elite_population = sorted(
                new_population,
                key=lambda x: calculate_itemset_utility(
                    x, vertical_data, horizontal_data
                ),
                reverse=True,
            )[:k]
            if new_elite_population == elite_population:
                generations_without_improvement += 1
            else:
                generations_without_improvement = 0
                elite_population = new_elite_population

        return elite_population
    except KeyError as e:
        print(f"Error: Item or transaction {e} not found in data.")
        return []


# Example usage
if __name__ == "__main__":
    vertical_data = {1: [0, 1, 2], 2: [0, 2], 3: [1, 2]}
    horizontal_data = {0: {1: 10, 2: 5}, 1: {1: 15, 3: 20}, 2: {2: 5, 3: 10}}
    external_utilities = {1: 10, 2: 5, 3: 15}

    top_k_itemsets = tkhuim_ga(
        vertical_data, horizontal_data, external_utilities, k=2, max_length=2
    )
    print("Top-k High Utility Itemsets:", top_k_itemsets)
