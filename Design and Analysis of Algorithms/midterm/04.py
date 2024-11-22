from typing import List, Dict, Tuple, Union


class Itemset:
    def __init__(self, items: List[str], tid: int, pu: int, nu: int, ru: int):
        """Initializes the Itemset class.

        Args:
            items (List[str]): _description_
            tid (int): _description_
            pu (int): _description_
            nu (int): _description_
            ru (int): _description_
        """
        self.items = items
        self.tid = tid
        self.pu = pu
        self.nu = nu
        self.ru = ru


class Mlist:
    def __init__(
        self,
        node_itemset: List[str],
        true_itemset: List[str],
        itemset_list: List[Itemset],
        prefix: List[str],
    ):
        """Initializes the Mlist class.

        Args:
            node_itemset (List[str]): _description_
            true_itemset (List[str]): _description_
            itemset_list (List[Itemset]): _description_
            prefix (List[str]): _description_
        """
        self.node_itemset = node_itemset
        self.true_itemset = true_itemset
        self.itemset_list = itemset_list
        self.prefix = prefix
        self.ru = 0
        self.pu = 0


def calculate_twu(database: List[Dict[str, Dict[str, int]]]) -> Dict[str, int]:
    """Calculate the Transaction Weighted Utility (TWU) for each item.

    Args:
        database (List[Dict[str, Dict[str, int]]]): _description_

    Returns:
        Dict[str, int]: _description_
    """
    twu = {}
    for transaction in database:
        for item in transaction:
            twu[item] = twu.get(item, 0) + transaction[item]["pu"]
    return twu


def calculate_maxper_avgper(
    database: List[Dict[str, Dict[str, int]]]
) -> Tuple[Dict[str, int], Dict[str, float]]:
    """Calculate maximum and average periodicity for items.

    Args:
        database (List[Dict[str, Dict[str, int]]]): _description_

    Returns:
        Tuple[Dict[str, int], Dict[str, float]]: _description_
    """
    maxper = {}
    avgper = {}
    last_tid = {}

    for tid, transaction in enumerate(database):
        for item in transaction:
            if item in last_tid:
                period = tid - last_tid[item]
                maxper[item] = max(maxper.get(item, 0), period)
            last_tid[item] = tid

    for item in last_tid:
        avgper[item] = len(database) / (last_tid[item] + 1)
    return maxper, avgper


def calculate_euics(
    database: List[Dict[str, Dict[str, int]]]
) -> Dict[Tuple[str, str], int]:
    """Calculate the Estimated Utility Co-occurrence Structure (EUCS).

    Args:
        database (List[Dict[str, Dict[str, int]]]): _description_

    Returns:
        Dict[Tuple[str, str], int]: _description_
    """
    euics = {}
    for transaction in database:
        items = list(transaction.keys())
        for i, item1 in enumerate(items):
            for item2 in items[i + 1 :]:
                pair = tuple(sorted((item1, item2)))
                euics[pair] = (
                    euics.get(pair, 0)
                    + transaction[item1]["pu"]
                    + transaction[item2]["pu"]
                )
    return euics


def generate_lists(
    database: List[Dict[str, Dict[str, int]]]
) -> Dict[str, List[Itemset]]:
    """Generate itemsets for each item.

    Args:
        database (List[Dict[str, Dict[str, int]]]): _description_

    Returns:
        Dict[str, List[Itemset]]: _description_
    """
    lists = {}
    for tid, transaction in enumerate(database):
        for item, values in transaction.items():
            ru = sum(v["pu"] for k, v in transaction.items() if k > item)
            if item not in lists:
                lists[item] = []
            lists[item].append(Itemset([item], tid, values["pu"], values["nu"], ru))
    return lists


def construct_list(
    prefix: List[str], list1: List[Itemset], list2: List[Itemset]
) -> List[Itemset]:
    """Combine two itemsets into a new itemset list.

    Args:
        prefix (List[str]): _description_
        list1 (List[Itemset]): _description_
        list2 (List[Itemset]): _description_

    Returns:
        List[Itemset]: _description_
    """
    new_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i].tid == list2[j].tid:
            new_list.append(
                Itemset(
                    prefix + list2[j].items,
                    list1[i].tid,
                    list1[i].pu + list2[j].pu,
                    list1[i].nu + list2[j].nu,
                    list2[j].ru,
                )
            )
            i += 1
            j += 1
        elif list1[i].tid < list2[j].tid:
            i += 1
        else:
            j += 1
    return new_list


def search(
    item_lists: List[List[Itemset]],
    item_utility: Dict[str, int],
    min_utility: int,
    min_per: int,
    max_per: int,
    min_avg: float,
    max_avg: float,
    euics: Dict[Tuple[str, str], int],
    database: List[Dict[str, Dict[str, int]]],
    results: List[Tuple[List[str], int]],
) -> None:
    """Recursive search for periodic high-utility itemsets

    Args:
        item_lists (List[List[Itemset]]): _description_
        item_utility (Dict[str, int]): _description_
        min_utility (int): _description_
        min_per (int): _description_
        max_per (int): _description_
        min_avg (float): _description_
        max_avg (float): _description_
        euics (Dict[Tuple[str, str], int]): _description_
        database (List[Dict[str, Dict[str, int]]]): _description_
        results (List[Tuple[List[str], int]]): _description_
    """
    for x_list in item_lists:
        x = x_list[0].items
        utility_x = sum(item.pu for item in x_list)
        ru_x = sum(item.ru for item in x_list)

        if utility_x >= min_utility:
            is_periodic = True
            last_tid = -1
            for item in x_list:
                if last_tid != -1 and not (min_per <= item.tid - last_tid <= max_per):
                    is_periodic = False
                    break
                last_tid = item.tid

            if is_periodic:
                avg_period = len(database) / (last_tid + 1)
                if min_avg <= avg_period <= max_avg:
                    results.append((x, utility_x))

        if ru_x + utility_x >= min_utility:
            new_lists = []
            for y_list in item_lists:
                y = y_list[0].items
                if x[-1] < y[-1]:
                    pair = tuple(sorted((x[-1], y[-1])))
                    if pair in euics and euics[pair] >= min_utility:
                        z_list = construct_list(x, x_list, y_list)
                        new_lists.append(z_list)
            search(
                new_lists,
                item_utility,
                min_utility,
                min_per,
                max_per,
                min_avg,
                max_avg,
                euics,
                database,
                results,
            )


def main():
    try:
        database = [
            {
                "a": {"pu": 15, "nu": -3},
                "b": {"pu": 12, "nu": 0},
                "d": {"pu": 24, "nu": 0},
                "c": {"pu": 3, "nu": -3},
            },
            {
                "a": {"pu": 3, "nu": 0},
                "d": {"pu": 12, "nu": 0},
                "c": {"pu": 3, "nu": -3},
            },
            {"a": {"pu": 3, "nu": 0}, "c": {"pu": 3, "nu": -3}},
            {"a": {"pu": 3, "nu": 0}},
            {"a": {"pu": 3, "nu": 0}},
            {
                "b": {"pu": 18, "nu": 0},
                "d": {"pu": 36, "nu": 0},
                "c": {"pu": 6, "nu": -6},
            },
            {"c": {"pu": 18, "nu": -18}},
        ]

        min_utility = 30
        min_per = 1
        max_per = 5
        min_avg = 1
        max_avg = 3

        twu = calculate_twu(database)
        maxper, avgper = calculate_maxper_avgper(database)
        item_utility = {
            item: sum(
                trx[item]["pu"] + trx[item]["nu"] for trx in database if item in trx
            )
            for item in twu
        }

        filtered_items = [
            item
            for item in twu
            if twu[item] >= min_utility
            and maxper[item] <= max_per
            and min_avg <= avgper[item] <= max_avg
        ]
        filtered_database = [
            {
                item: values
                for item, values in transaction.items()
                if item in filtered_items
            }
            for transaction in database
        ]

        euics = calculate_euics(filtered_database)
        lists = generate_lists(filtered_database)

        sorted_items = sorted(
            filtered_items,
            key=lambda item: (-1 if item_utility[item] < 0 else 1, twu[item]),
        )

        results = []
        search(
            [lists[item] for item in sorted_items],
            item_utility,
            min_utility,
            min_per,
            max_per,
            min_avg,
            max_avg,
            euics,
            database,
            results,
        )

        if results:
            for itemset, utility in results:
                print(f"Itemset: {itemset} with Utility: {utility}")

            print("=================================")
            highest_utility_itemset = max(results, key=lambda x: x[1])
            print(
                f"Highest Utility Itemset: {highest_utility_itemset[0]} with Utility: {highest_utility_itemset[1]}"
            )
        else:
            print("No periodic high-utility itemsets found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
