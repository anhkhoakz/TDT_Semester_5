import itertools
# Dataset
transactions = [
    {"Tid": "T1", "Items": {"a": 5, "b": 2, "c": 1, "d": 2}},
    {"Tid": "T2", "Items": {"a": 1, "c": 1, "d": 1, "g": 3}},
    {"Tid": "T3", "Items": {"a": 1, "c": 1, "f": 1}},
    {"Tid": "T4", "Items": {"a": 1, "f": 4, "g": 2}},
    {"Tid": "T5", "Items": {"a": 1, "g": 2}},
    {"Tid": "T6", "Items": {"b": 3, "c": 2, "d": 3, "e": 1}},
    {"Tid": "T7", "Items": {"c": 6, "e": 4}},
    {"Tid": "T8", "Items": {"e": 1, "f": 3}},
]

unit_utilities = {"a": 3, "b": 6, "c": -3, "d": 12, "e": -5, "f": -2, "g": -1}
minUtility = 30
minPer = 1
maxPer = 5
minAvg = 1
maxAvg = 3

# Helper functions
def calculate_twu_and_periodicity(database):
    """
    Calculate the Total Weight Utility (TWU) and periodic information for each item.
    """
    twu = {}
    item_periods = {}
    
    for idx, transaction in enumerate(database):
        positive_utility = sum(qty * unit_utilities.get(item, 0) for item, qty in transaction["Items"].items() if unit_utilities.get(item, 0) > 0)

        for item, qty in transaction["Items"].items():
            if item not in twu:
                twu[item] = 0

            if item not in item_periods:
                item_periods[item] = []
                
            twu[item] += positive_utility
            item_periods[item].append(idx + 1)  # Record the transaction index

    max_per = {}
    avg_per = {}
    min_per = {}
    for item in item_periods:
        max_per_item = 0
        min_per_item = 999999
        avg_per_item = 0
        current_period = 0
        for idx in item_periods[item]:
            if idx - current_period > max_per_item:
                max_per_item = idx - current_period

            if idx - current_period < min_per_item:
                min_per_item = idx - current_period
            

            current_period = idx


        avg_per_item = (max(item_periods[item]) +1) / (len(item_periods[item]) +1 )
        max_per[item] = max_per_item
        min_per[item] = min_per_item
        avg_per[item] = avg_per_item

    return twu, max_per, avg_per, min_per




def prune_items(minUtility, maxPer, minPer, minAvg, maxAvg,twu, max_per, min_per, avg_per):
    """
    Prune items that do not meet the threshold conditions.
    """
    sorted_twu = dict(sorted(twu.items(), key=lambda item: item[1]))

    return {
        item: True
        for item in sorted_twu
        if max_per[item] <= maxPer and min_per[item] >= minPer and avg_per[item] >= minAvg and avg_per[item] <= maxAvg and twu[item] >= minUtility
    }

def reorder_database(database, pruned_items):
   return [
        {
            "Tid": transaction["Tid"],
            "Items": {
                item: transaction["Items"][item]
                for item in pruned_items
                if item in transaction["Items"] 
            }
        }
        for transaction in database
        if any(item in transaction["Items"] for item in pruned_items)
    ]



def build_eucs(database, unit_utilities, min_utility, items):
    """
    Build the Estimated Utility Co-occurrence Structure (EUCS).
    """
    eucs = {}

    for i1, i2 in itertools.combinations((items), 2):
        twu_pair = 0
        for transaction in database:
            
            if i1 in transaction["Items"] and i2 in transaction["Items"]:
                twu_pair += sum(
                    qty * unit_utilities.get(item, 0)
                    for item, qty in transaction["Items"].items()
                )
            
        if twu_pair >= min_utility:
            eucs[(i1, i2)] = twu_pair

    return eucs


def pnu_list(database, unit_utilities, eucs):
    """
    Generate the PNU list for all itemsets in the EUCS.
    
    Args:
        database (list): List of transactions, each as a dictionary with Tid and Items.
        unit_utilities (dict): Dictionary of unit utilities for each item.
        eucs (dict): Estimated Utility Co-occurrence Structure containing item pairs.
    
    Returns:
        dict: PNU list, where each key is an itemset (tuple), and the value is a list of tuples
              (Tid, positive utility, negative utility, remaining utility).
    """
    pnu = {}
    
    # Iterate through all itemsets in the EUCS
    for (i1, i2) in eucs:
        # Initialize the PNU list for the current itemset
        pnu[(i1, i2)] = []
        
        for transaction in database:
            # Check if the itemset (i1, i2) is in the current transaction
            if i1 in transaction["Items"] and i2 in transaction["Items"]:
                
                # Calculate positive and negative utilities for the itemset
                pos_utility = sum(
                    transaction["Items"][item] * unit_utilities.get(item, 0)
                    for item in {i1, i2}
                    if unit_utilities.get(item, 0) > 0
                )
                neg_utility = sum(
                    transaction["Items"][item] * unit_utilities.get(item, 0)
                    for item in {i1, i2}
                    if unit_utilities.get(item, 0) < 0
                )
                
                # Calculate the remaining utility in the transaction
                remaining_utility = sum(
                    transaction["Items"][item] * unit_utilities.get(item, 0)
                    for item in transaction["Items"]
                    if item not in {i1, i2}
                )
                
                # Append the tuple to the PNU list for the itemset
                pnu[(i1, i2)].append((
                    transaction["Tid"],  # Transaction ID
                    pos_utility,         # Positive utility
                    neg_utility,         # Negative utility
                    remaining_utility    # Remaining utility
                ))
    
    return pnu


    """
    Construct initial Mlist for single items.
    
    Args:
        database (list): List of transactions, each as a dictionary with Tid and Items.
        unit_utilities (dict): Utility values for each item.

    Returns:
        dict: Mlist structure for single items.
    """
    mlist = {}

    for transaction in database:
        tid = transaction["Tid"]
        for item, qty in transaction["Items"].items():
            pos_utility = qty * unit_utilities[item] if unit_utilities[item] > 0 else 0
            neg_utility = qty * unit_utilities[item] if unit_utilities[item] < 0 else 0
            rem_utility = sum(
                qty * unit_utilities[other_item]
                for other_item, qty in transaction["Items"].items()
                if other_item != item
            )

            if (item,) not in mlist:
                mlist[(item,)] = []

            mlist[(item,)].append((tid, pos_utility, neg_utility, rem_utility))

    return mlist

def calculate_itemset_periodicity(itemset, database):
    """
    Calculate the periodicity details (minPer, maxPer, avgPer) for an itemset.
    """
    transaction_ids = []
    for transaction in database:
        if all(item in transaction["Items"] for item in itemset):
            transaction_ids.append(int(transaction["Tid"][1:]))

    if not transaction_ids:
        return None, None, None

    transaction_ids = sorted(transaction_ids)
    periods = [transaction_ids[i] - transaction_ids[i - 1] for i in range(1, len(transaction_ids))]
    
    if not periods:
        return 0, 0, transaction_ids[0]  # Single transaction case

    minPer = min(periods)
    maxPer = max(periods)
    avgPer = sum(periods) / len(periods)
    return minPer, maxPer, avgPer


def calculate_remaining_utility(itemset, transaction, unit_utilities):
    """
    Calculate the Remaining Utility (RU) for a given itemset in a transaction.
    """
    items_in_transaction = transaction["Items"]
    remaining_items = [item for item in items_in_transaction if item > max(itemset)]
    remaining_utility = sum(
        items_in_transaction[item] * unit_utilities.get(item, 0) for item in remaining_items
    )
    return remaining_utility






def prepare_phmn_plus(database, min_utility,maxPer, minPer, maxAvg, minAvg):
    """
    The preparation procedure for PHMN+ which calculates item utilities and prepares data for formal mining.
    """
    # Step 1: Calculate TWU and Periodicity (maxPer and avgPer)
    twu, max_per, avg_per, min_per = calculate_twu_and_periodicity(database)
    
    print("TWU:", twu)
    print("Max Periodicity:", max_per)
    print("Avg Periodicity:", avg_per)
    print("Min Periodicity:", min_per)

   


    # Step 3: Prune items that do not meet the threshold conditions
    pruned_items = prune_items(min_utility, maxPer, minPer, minAvg, maxAvg, twu,max_per, min_per, avg_per).keys()
    
    print("Pruned Items:", pruned_items)

    # Step 4: Reorder the database
    reordered_db = reorder_database(database, pruned_items)

    print("Reordered Database:", reordered_db)

    # Step 5: Build the Estimated Utility Co-occurrence Structure (EUCS)
    eucs = build_eucs(reordered_db, unit_utilities, min_utility, pruned_items)

    print("EUCS:", eucs)

    pnu = pnu_list(reordered_db, unit_utilities, eucs)
    print("PNU:", pnu)




    return  reordered_db , eucs, pnu




def calculate_utility(itemset, transactions):
    total_utility = 0
    for transaction in transactions:
        if all(item in transaction["Items"] for item in itemset):
            total_utility += sum(transaction["Items"][item] for item in itemset)
    return total_utility

# Hàm kiểm tra periodicity
def check_periodicity(itemset, transactions, min_per, max_per):
    indices = [i for i, transaction in enumerate(transactions) if all(item in transaction["Items"] for item in itemset)]
    if not indices:
        return False, None
    periods = [indices[i] - indices[i-1] for i in range(1, len(indices))]
    max_period = max(periods, default=0)
    avg_period = sum(periods) / len(periods) if periods else 0
    return min_per <= max_period <= max_per, avg_period


def search(prefix, prefix_list, lists, transactions, min_per, max_per, min_avg, max_avg, min_utility):
    periodic_high_utility_itemsets = []

    for itemset in lists:
        # Tính utility và kiểm tra periodicity
        utility = calculate_utility(itemset, transactions)
        satisfies_periodicity, avg_period = check_periodicity(itemset, transactions, min_per, max_per)

        # Nếu thỏa mãn điều kiện periodicity và utility, thêm vào kết quả
        if utility >= min_utility and satisfies_periodicity:
            periodic_high_utility_itemsets.append((itemset, utility))
        
        # Kiểm tra điều kiện Remaining Utility (RU) để mở rộng
        if utility >= min_utility and satisfies_periodicity:
            new_lists = []
            for next_itemset in lists:
                if set(itemset) < set(next_itemset):  # Thứ tự từ điển
                    combined_itemset = tuple(sorted(set(itemset) | set(next_itemset)))

                    # Kiểm tra EUCP và tính utility của tập hợp mở rộng
                    if combined_itemset not in prefix_list:
                        new_lists.append(combined_itemset)

            # Đệ quy với tập hợp mở rộng mới
            if new_lists:
                periodic_high_utility_itemsets.extend(
                    search(itemset, prefix_list, new_lists, transactions, min_per, max_per, min_avg, max_avg, min_utility)
                )

    return periodic_high_utility_itemsets

# Main Algorithm
def phmn_algorithm(database, min_utility, maxPer,minPer, maxAvg, minAvg):
    """
    Perform the formal mining of periodic high-utility itemsets after preparation.
    """
    # Step 1: Prepare data for PHMN+
    reordered_db, eucs, pnu_list = prepare_phmn_plus(database, min_utility,maxPer, minPer, minAvg, maxAvg)
    
    # Step 2: Start mining high-utility itemsets

    # search(set(), database, initial_lists, database, minPer, maxPer, minAvg, maxAvg, min_utility)

    return None



# Run the program
a = phmn_algorithm(transactions, minUtility, maxPer, minPer, minAvg, maxAvg)

