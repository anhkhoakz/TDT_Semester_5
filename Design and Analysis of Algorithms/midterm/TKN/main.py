import heapq

# Define the priority queue for top-k high utility itemsets
TKHQ = []


def read_data(file_name: str) -> dict:
    """Read and parse transaction data from a file."""
    with open(file_name, "r") as file:
        data = file.read()
    return eval(data)


def process_data(dataset: list) -> tuple:
    """Process dataset to extract transactions and item profits."""
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
    """Calculate Positive Item Utility (PRIU) for each item."""
    priu = {}
    for transaction in transactions.values():
        for item, quantity in transaction.items():
            utility = quantity * profits.get(item, 0)
            priu[item] = priu.get(item, 0) + utility
    return priu


def priu_strategy(priu_dict: dict, k: int) -> float:
    """Determine minimum utility threshold using PRIU strategy."""
    priu_values = sorted(priu_dict.values(), reverse=True)
    if k <= len(priu_values):
        return priu_values[k - 1]
    return priu_values[-1]


def filter_transactions(transactions: dict, secondary_items: list) -> dict:
    """Filter transactions to retain only items in Secondary(a)."""
    filtered = {}
    secondary_set = set(secondary_items)
    for tid, items in transactions.items():
        filtered_items = {
            item: qty for item, qty in items.items() if item in secondary_set
        }
        if filtered_items:
            filtered[tid] = filtered_items
    return filtered


def sort_secondary_items(secondary_items: list, ptwu: dict, profits: dict) -> list:
    """Sort items in Secondary(a) based on total order."""
    positive_items = {
        item: ptwu[item] for item in secondary_items if profits.get(item, 0) > 0
    }
    negative_items = {
        item: ptwu[item] for item in secondary_items if profits.get(item, 0) < 0
    }

    sorted_positive = sorted(positive_items, key=positive_items.get)
    sorted_negative = sorted(negative_items, key=negative_items.get)
    return sorted_positive + sorted_negative


def transform_to_utilities(transactions: dict, profits: dict) -> list:
    """Transform transaction database into utilities."""
    utilities = []
    for items in transactions.values():
        transformed = {item: profits[item] * qty for item, qty in items.items()}
        utilities.append(transformed)
    return utilities


def calculate_psu(database: list, itemset: list, target: str) -> float:
    """Calculate PSU for an item in the database."""
    psu = 0
    for transaction in database:
        if target in transaction:
            item_utility = transaction[target] + sum(
                transaction.get(i, 0) for i in itemset
            )
            psu += item_utility
    return psu


def search(
    alpha, utility, eta, projected, primary_items, secondary_items, min_util, ptwu, k
):
    """Perform depth-first search to find top-k high utility itemsets."""
    global TKHQ

    for z in primary_items:
        beta = alpha + [z]
        beta_utility = utility + calculate_psu(projected, beta, z)

        if beta_utility >= min_util:
            heapq.heappush(TKHQ, (beta_utility, beta))
            if len(TKHQ) > k:
                heapq.heappop(TKHQ)
            if len(TKHQ) == k:
                min_util = min(TKHQ, key=lambda x: x[0])[0]

        remaining_secondary = secondary_items[secondary_items.index(z) + 1 :]
        psu_remaining = {
            w: calculate_psu(projected, beta, w) for w in remaining_secondary
        }
        primary_beta = [w for w, psu in psu_remaining.items() if psu >= min_util]
        search(
            beta,
            beta_utility,
            eta,
            projected,
            primary_beta,
            remaining_secondary,
            min_util,
            ptwu,
            k,
        )


def TKN_algorithm(dataset: list, k: int):
    """Main TKN algorithm to find top-k high utility itemsets."""
    transactions, profits = process_data(dataset)
    priu = calculate_priu(transactions, profits)
    min_util = priu_strategy(priu, k)

    # Calculate PTWU (Positive Transaction-Weighted Utility)
    ptwu = {
        item: sum(
            items[item] * profits[item]
            for tid, items in transactions.items()
            if item in items
        )
        for item in profits
    }

    secondary_items = [item for item, utility in priu.items() if utility >= min_util]
    sorted_secondary = sort_secondary_items(secondary_items, ptwu, profits)

    filtered_transactions = filter_transactions(transactions, sorted_secondary)
    projected_database = transform_to_utilities(filtered_transactions, profits)

    primary_items = [
        item
        for item in sorted_secondary
        if calculate_psu(projected_database, [], item) >= min_util
    ]
    search(
        [],
        0,
        set(),
        projected_database,
        primary_items,
        sorted_secondary,
        min_util,
        ptwu,
        k,
    )

    return sorted(TKHQ, key=lambda x: -x[0])


def read_data(file_name: str) -> dict:

    with open(file_name, "r") as file:
        data = file.read()

    dataset = eval(data)
    return dataset


# Example Usage
dataset = read_data("data.txt")

k = 3
result = TKN_algorithm(dataset, k)
print("Top-k High Utility Itemsets:", result)
