from collections import defaultdict, namedtuple
from datetime import datetime

# Define the transaction and utility entries similar to the report
TransactionEntry = namedtuple(
    "TransactionEntry", ["transaction_id", "utility", "recency", "remaining_utility"]
)

# Dataset from Report - Manually Defined
transaction_data = [
    {"Tid": 1, "Timestamp": "2020-06-20 09:30", "Items": {"b": 2, "d": 6}},
    {"Tid": 2, "Timestamp": "2020-06-20 10:45", "Items": {"a": 5, "b": 3, "c": 20}},
    {"Tid": 3, "Timestamp": "2020-06-20 12:55", "Items": {"c": 10, "e": 6}},
    {"Tid": 4, "Timestamp": "2020-06-22 17:23", "Items": {"d": 6, "e": 3}},
    {"Tid": 5, "Timestamp": "2020-06-22 22:42", "Items": {"a": 30, "c": 40, "d": 10}},
    {"Tid": 6, "Timestamp": "2020-06-23 14:34", "Items": {"b": 3, "c": 20}},
    {"Tid": 7, "Timestamp": "2020-06-23 11:05", "Items": {"d": 2, "e": 6}},
    {"Tid": 8, "Timestamp": "2020-06-24 08:57", "Items": {"c": 20, "d": 4}},
    {
        "Tid": 9,
        "Timestamp": "2020-06-24 21:20",
        "Items": {"a": 15, "b": 2, "c": 20, "d": 2},
    },
    {
        "Tid": 10,
        "Timestamp": "2020-06-25 13:11",
        "Items": {"a": 10, "b": 3, "c": 50, "e": 6},
    },
]

external_utilities = {"a": 5, "b": 1, "c": 10, "d": 2, "e": 3}

# Parse timestamps for recency calculations
for transaction in transaction_data:
    transaction["Timestamp"] = datetime.strptime(
        transaction["Timestamp"], "%Y-%m-%d %H:%M"
    )


# Calculate transaction utility
def calculate_transaction_utility(transaction, external_utilities):
    return sum(
        qty * external_utilities[item] for item, qty in transaction["Items"].items()
    )


# Calculate recency using a decay factor
def calculate_recency(transaction_date, current_date, decay_factor=0.1):
    days_diff = (current_date - transaction_date).days
    return (1 - decay_factor) ** days_diff


# Step 1: Initial Scan to Calculate twut, recency values, and filter items
def initial_scan(
    transaction_data, external_utilities, min_util, min_rec, decay_factor=0.1
):
    item_twut = defaultdict(int)
    item_recency = defaultdict(float)
    current_date = max(transaction["Timestamp"] for transaction in transaction_data)

    # Calculate twut and recency for each item
    for transaction in transaction_data:
        tut = calculate_transaction_utility(transaction, external_utilities)
        for item, qty in transaction["Items"].items():
            item_twut[item] += tut
            item_recency[item] += calculate_recency(
                transaction["Timestamp"], current_date, decay_factor
            )

    # Filter items
    filtered_items = {
        item
        for item, twut in item_twut.items()
        if twut >= min_util and item_recency[item] >= min_rec
    }
    return filtered_items, item_twut, item_recency


# Step 2: Construct Recent Short Period Utility List (RSPUL)
def construct_rspul(
    transaction_data, filtered_items, external_utilities, decay_factor=0.1
):
    rspul = defaultdict(list)
    current_date = max(transaction["Timestamp"] for transaction in transaction_data)

    for transaction in transaction_data:
        for item in transaction["Items"]:
            if item in filtered_items:
                utility = transaction["Items"][item] * external_utilities[item]
                recency = calculate_recency(
                    transaction["Timestamp"], current_date, decay_factor
                )
                remaining_utility = sum(
                    qty * external_utilities[it]
                    for it, qty in transaction["Items"].items()
                    if it != item
                )
                rspul[item].append(
                    TransactionEntry(
                        transaction["Tid"], utility, recency, remaining_utility
                    )
                )
    return rspul


# Step 3: Mining Top-K RSPHUIs using RSPUL and Pruning
def mine_rsphui(rspul, min_rec, max_per, k):
    rsphui_candidates = []

    for item, entries in rspul.items():
        total_utility = sum(entry.utility for entry in entries)
        total_recency = sum(entry.recency for entry in entries)
        max_period = max(
            entries[i + 1].transaction_id - entries[i].transaction_id
            for i in range(len(entries) - 1)
        )

        # Apply recency and maximum period constraints
        if total_recency >= min_rec and max_period <= max_per:
            rsphui_candidates.append((item, total_utility, total_recency, max_period))

    # Sort by utility to get the Top-K
    rsphui_candidates = sorted(rsphui_candidates, key=lambda x: x[1], reverse=True)[:k]
    return rsphui_candidates


# Main function to execute the algorithm
def run_rsphuim_algorithm(
    transaction_data, external_utilities, min_util=100, min_rec=1.0, max_per=6, k=2
):
    filtered_items, item_twut, item_recency = initial_scan(
        transaction_data, external_utilities, min_util, min_rec
    )
    rspul = construct_rspul(transaction_data, filtered_items, external_utilities)
    top_k_rsphui = mine_rsphui(rspul, min_rec, max_per, k)

    return top_k_rsphui


# Run the algorithm
top_k_rsphui = run_rsphuim_algorithm(transaction_data, external_utilities)
print("Top-K Recent Short Period High Utility Itemsets:")
for item, utility, recency, period in top_k_rsphui:
    print(f"Item: {item}, Utility: {utility}, Recency: {recency}, Period: {period}")


# https://chatgpt.com/share/67345e64-6038-8006-b1c6-8a08cb50d2de
