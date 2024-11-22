from collections import defaultdict, namedtuple
from itertools import combinations
from datetime import datetime

import os


def file_to_path(filename):
    """
    Get the absolute path of a file.
    :param filename: the name of the file
    :return: the absolute path
    """
    return os.path.abspath(filename)
# Define the transaction and utility entries similar to the report
TransactionEntry = namedtuple("TransactionEntry", ["transaction_id", "utility", "recency", "remaining_utility"])

# Dataset from Report - Manually Defined
input = file_to_path("./transactions.csv")

with open(input, "r") as file:
    transaction_data = []
    for line in file:
        tid, timestamp, items = line.strip().split(",")  # Split by comma
        items = {item: int(qty) for item, qty in (pair.split(":") for pair in items.split(" "))}

        # timestamp has format 20/06/2020 09:30
        timestamp = timestamp.replace("/", "-")

        separate = timestamp.split(" ")
        date = separate[0]
        
        date = date.split("-")
        date = date[2] + "-" + date[1] + "-" + date[0]
        timestamp = date + " " + separate[1]


        transaction_data.append({"Tid": int(tid), "Timestamp": datetime.strptime(timestamp, "%Y-%m-%d %H:%M"), "Items": items})



input = file_to_path("./external_utilities.csv")

with open(input, "r") as file:
    external_utilities = {}
    for line in file:
        item, utility = line.strip().split(":")
        external_utilities[item] = int(utility)



# Calculate utility and recency
def calculate_transaction_utility(transaction, external_utilities):
    return sum(qty * external_utilities[item] for item, qty in transaction["Items"].items())

def calculate_recency(transaction_date, current_date, decay_factor=0.1):
    days_diff = (current_date - transaction_date).days  # Now this will work correctly
    return (1 - decay_factor) ** days_diff


# Step 1: Calculate TWU, recency, and filter items
def initial_scan(transaction_data, external_utilities, min_util, min_rec, decay_factor=0.1):
    item_twut = defaultdict(int)
    item_recency = defaultdict(float)
    current_date = max(transaction["Timestamp"] for transaction in transaction_data)
    for transaction in transaction_data:
        tut = calculate_transaction_utility(transaction, external_utilities)
        for item, qty in transaction["Items"].items():
            item_twut[item] += tut
            item_recency[item] += calculate_recency(transaction["Timestamp"], current_date, decay_factor)
    filtered_items = {item for item in item_twut if item_twut[item] >= min_util and item_recency[item] >= min_rec}
    return filtered_items, item_twut, item_recency


# Step 2: Construct RSPUL for individual and paired itemsets
def construct_rspul(transaction_data, filtered_items, external_utilities, decay_factor=0.1):
    rspul = defaultdict(list)
    current_date = max(transaction["Timestamp"] for transaction in transaction_data)
    
    for transaction in transaction_data:
        items = [item for item in transaction["Items"] if item in filtered_items]
        for itemset in items + list(combinations(items, 2)):  # Support pairs of items
            if isinstance(itemset, str):  # Single item
                itemset = (itemset,)
            utility = sum(transaction["Items"][i] * external_utilities[i] for i in itemset)
            recency = calculate_recency(transaction["Timestamp"], current_date, decay_factor)
            remaining_utility = sum(
                qty * external_utilities[it] for it, qty in transaction["Items"].items() if it not in itemset
            )
            rspul[itemset].append(TransactionEntry(transaction["Tid"], utility, recency, remaining_utility))
    return rspul

# Step 3: Mining Top-K RSPHUIs using RSPUL and Pruning
def mine_rsphui(rspul, min_rec, max_per, k):
    rsphui_candidates = []

    for itemset, entries in rspul.items():
        if not entries:
            continue  # Skip empty entries list

        total_utility = sum(entry.utility for entry in entries)
        total_recency = sum(entry.recency for entry in entries)

        # Calculate maximum period if entries has more than one element
        if len(entries) > 1:
            max_period = max(entries[i + 1].transaction_id - entries[i].transaction_id for i in range(len(entries) - 1))
        else:
            max_period = 0  # Define max_period as 0 when there's only one entry, assuming it's within the max_per threshold

        # Apply recency and maximum period constraints
        if total_recency >= min_rec and max_period <= max_per:
            rsphui_candidates.append((itemset, total_utility, total_recency, max_period))

    # Sort by utility to get the Top-K
    rsphui_candidates = sorted(rsphui_candidates, key=lambda x: x[1], reverse=True)[:k]
    return rsphui_candidates


# Main function
def run_rsphuim_algorithm(transaction_data, external_utilities, min_util=30, min_rec=1.0, max_per=5, k=10):
    filtered_items, item_twut, item_recency = initial_scan(transaction_data, external_utilities, min_util, min_rec)
    rspul = construct_rspul(transaction_data, filtered_items, external_utilities)
    top_k_rsphui = mine_rsphui(rspul, min_rec, max_per, k)
    return top_k_rsphui

# Run the algorithm
top_k_rsphui = run_rsphuim_algorithm(transaction_data, external_utilities)
print("Top-K Recent Short Period High Utility Itemsets:")
for itemset, utility, recency, period in top_k_rsphui:
    print(f"Itemset: {itemset}, Utility: {utility}, Recency: {recency}, Period: {period}")
