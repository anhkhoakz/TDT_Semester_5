import heapq


# Main function
def main():
    global TKHQ
    TKHQ = []

    # Define the input file name and the top-k value
    file_name = "data.txt"
    k = 4

    # Read the data
    dataset = read_data(file_name)

    # Process the data
    transactions, profits = process_data(dataset)

    # Run the Top-k High-Utility Itemset (TKN) algorithm
    TKN_algorithm(transactions, profits, k)


# Helper functions
def read_data(file_name: str) -> dict:
    """Read and parse data from a file."""
    with open(file_name, "r") as file:
        data = file.read()
    return eval(data)


def process_data(dataset: list) -> tuple:
    """Process a dataset to extract transactions and item profits."""
    transactions = {}
    profits = {}

    for entry in dataset:
        tid = entry["TID"].lower()
        items = entry["items"]
        quantities = entry["quantities"]
        profit_list = entry["profit"]

        transactions[tid] = {item: qty for item, qty in zip(items, quantities)}
        for item, profit in zip(items, profit_list):
            if item not in profits:
                profits[item] = profit

    return transactions, profits


def calculate_priu(transactions: dict, profits: dict) -> dict:
    """Calculate the Positive Item Utility (PRIU) for each item."""
    priu_dict = {}
    for transaction in transactions.values():
        for item, quantity in transaction.items():
            utility = quantity * profits.get(item, 0)
            priu_dict[item] = priu_dict.get(item, 0) + utility
    return priu_dict


def calculate_ptwu(transactions: dict, profits: dict) -> dict:
    """Calculate the Positive Transactional Utility (PTWU) for each item."""
    ptwu = {item: 0 for transaction in transactions.values() for item in transaction}
    for items in transactions.values():
        for item, quantity in items.items():
            if profits.get(item, 0) > 0:
                ptwu[item] += quantity * profits[item]
    return ptwu


def priu_strategy(priu_dict: dict, k: int) -> float:
    """Determine the k-th highest PRIU value as the utility threshold."""
    priu_values = sorted(priu_dict.values(), reverse=True)
    return priu_values[k - 1] if k <= len(priu_values) else priu_values[-1]


def sort_secondary_a_by_total_order(
    secondary_a: set, ptwu: dict, profits: dict
) -> list:
    """Sort items in secondary_a based on total order (positive and negative groups)."""
    positive_items = {
        item: ptwu[item] for item in secondary_a if profits.get(item, 0) > 0
    }
    negative_items = {
        item: ptwu[item] for item in secondary_a if profits.get(item, 0) < 0
    }
    sorted_positive = sorted(positive_items, key=lambda x: positive_items[x])
    sorted_negative = sorted(negative_items, key=lambda x: negative_items[x])
    return sorted_positive + sorted_negative


def filter_transactions_by_secondary_a(
    transactions: dict, sorted_secondary_a: list
) -> dict:
    """Filter transactions based on items in sorted_secondary_a."""
    secondary_set = set(sorted_secondary_a)
    return {
        tid: {item: qty for item, qty in items.items() if item in secondary_set}
        for tid, items in transactions.items()
        if any(item in secondary_set for item in items)
    }


def sort_transaction_items_by_total_order(
    transactions: dict, sorted_secondary_a: list
) -> dict:
    """Sort items in each transaction by their order in sorted_secondary_a."""
    item_order = {item: index for index, item in enumerate(sorted_secondary_a)}
    return {
        tid: dict(
            sorted(
                items.items(), key=lambda item: item_order.get(item[0], float("inf"))
            )
        )
        for tid, items in transactions.items()
    }


def transform_to_utilities(transactions: dict, profits: dict) -> list:
    """Convert transactions to profit-based utilities."""
    return [
        {item: qty * profits.get(item, 0) for item, qty in items.items()}
        for items in transactions.values()
    ]


def calculate_psu(database: list, itemset: list, target_item: str) -> float:
    """Calculate the PSU for a set and a target item."""
    psu = 0
    for transaction in database:
        if target_item in transaction:
            start_counting = False
            item_utility = 0
            rru = 0
            for i in transaction:
                if (all(item in transaction for item in itemset)) or not itemset:
                    if i == target_item:
                        start_counting = True
                        item_utility = transaction[i]
                    elif start_counting and transaction[i] > 0:
                        rru += transaction[i]
            psu += item_utility + rru
    return psu


def LIUS_Build_contiguous(sorted_database: list, priu_list: dict) -> list:
    """Build a LIUS matrix for contiguous itemsets."""
    items = list(priu_list.keys())
    n = len(items)
    lius_matrix = [[None for _ in range(n)] for _ in range(n)]
    for transaction in sorted_database:
        for i in range(n):
            cumulative_utility = 0
            for j in range(i + 1, n):
                contiguous_sequence = items[i : j + 1]
                utility = sum(transaction.get(item, 0) for item in contiguous_sequence)
                cumulative_utility += utility
                if lius_matrix[i][j] is None:
                    lius_matrix[i][j] = {"sequence": contiguous_sequence, "utility": 0}
                lius_matrix[i][j]["utility"] += utility
    return lius_matrix


def search(
    alpha,
    prefix_utility,
    eta,
    projected_dataset,
    primary_items,
    secondary_items,
    minUtil,
    ptwu,
    k,
):
    """Perform DFS to find top-k HUIs."""
    global TKHQ
    for z in primary_items:
        beta = alpha + [z]
        beta_utility = calculate_utility_all(projected_dataset, beta)
        if beta_utility >= minUtil:
            TKHQ.append((beta, beta_utility))
            TKHQ = sorted(TKHQ, key=lambda x: x[1], reverse=True)
            if len(TKHQ) > k:
                TKHQ.pop()
            if len(TKHQ) == k:
                minUtil = TKHQ[-1][1]


def calculate_utility_all(database, itemset):
    """Calculate total utility of an itemset in a database."""
    return sum(
        sum(transaction.get(item, 0) for item in itemset) for transaction in database
    )


def TKN_algorithm(transactions: dict, profits: dict, k: int) -> None:
    """Run the Top-k High-Utility Itemset algorithm."""
    global TKHQ
    Alpha = []
    minUtil = 0

    priu_dict = calculate_priu(transactions, profits)
    g = {item for item, utility in priu_dict.items() if utility < 0}
    ptwu = calculate_ptwu(transactions, profits)
    minUtil = priu_strategy(priu_dict, k)
    secondary_a = {item for item, ptwu_value in ptwu.items() if ptwu_value >= minUtil}
    sorted_secondary_a = sort_secondary_a_by_total_order(secondary_a, ptwu, profits)
    filtered_transactions = filter_transactions_by_secondary_a(
        transactions, sorted_secondary_a
    )
    sorted_transactions = sort_transaction_items_by_total_order(
        filtered_transactions, sorted_secondary_a
    )
    db_transform = transform_to_utilities(sorted_transactions, profits)

    primary_items = [
        item
        for item in sorted_secondary_a
        if calculate_psu(db_transform, Alpha, item) >= minUtil
    ]

    search(
        Alpha, 0, g, db_transform, primary_items, sorted_secondary_a, minUtil, ptwu, k
    )

    print("Result:", TKHQ[:k])


if __name__ == "__main__":
    main()
