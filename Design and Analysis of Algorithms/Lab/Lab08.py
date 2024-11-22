from typing import List, Tuple, Dict
import heapq


# Activity Selection Problem
def activity_selection(activities: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Selects the maximum number of activities that don't overlap.

    Args:
        activities (List[Tuple[int, int]]): List of activities with (start, finish) times.

    Returns:
        List[Tuple[int, int]]: List of selected activities.
    """
    # Sort activities by their finish time
    activities.sort(key=lambda x: x[1])

    # Select the first activity
    selected_activities = [activities[0]]
    last_finish_time = activities[0][1]

    for i in range(1, len(activities)):
        if activities[i][0] >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = activities[i][1]

    return selected_activities


# Job Scheduling Problem
def job_scheduling(
    tasks: List[Tuple[int, int]], max_deadline: int
) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Schedules tasks to maximize profit within given deadlines.

    Args:
        tasks (List[Tuple[int, int]]): List of tasks with (deadline, profit).
        max_deadline (int): Maximum deadline allowed.

    Returns:
        Tuple[int, List[Tuple[int, int]]]: Total profit and list of scheduled tasks.
    """
    # Sort tasks by profit in decreasing order
    tasks.sort(key=lambda x: x[1], reverse=True)

    # Array to keep track of free time slots
    slots = [-1] * max_deadline
    total_profit = 0

    for task in tasks:
        # Check for a free slot from the deadline backwards
        for j in range(min(max_deadline - 1, task[0] - 1), -1, -1):
            if slots[j] == -1:
                slots[j] = task
                total_profit += task[1]
                break

    return total_profit, [slot for slot in slots if slot != -1]


# Prim's Algorithm
def prim(graph: Dict[int, List[Tuple[int, int]]], start: int) -> List[Tuple[int, int]]:
    """
    Finds the Minimum Spanning Tree (MST) of a graph using Prim's algorithm.

    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Graph represented as an adjacency list.
        start (int): Starting vertex.

    Returns:
        List[Tuple[int, int]]: Edges in the MST.
    """
    mst = []
    visited = set()
    min_heap = [(0, start)]  # (weight, vertex)

    while min_heap:
        weight, current = heapq.heappop(min_heap)
        if current not in visited:
            visited.add(current)
            mst.append((weight, current))
            for neighbor, edge_weight in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor))

    return mst


# Union-Find Class
class UnionFind:
    def __init__(self, n: int):
        """
        Initializes the Union-Find data structure.

        Args:
            n (int): Number of elements.
        """
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        """
        Finds the representative of the set containing x.

        Args:
            x (int): Element.

        Returns:
            int: Representative element.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        """
        Unites two sets containing x and y.

        Args:
            x (int): First element.
            y (int): Second element.
        """
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


# Kruskal's Algorithm
def kruskal(
    edges: List[Tuple[int, int, int]], n: int
) -> Tuple[List[Tuple[int, int, int]], int]:
    """
    Finds the Minimum Spanning Tree (MST) of a graph using Kruskal's algorithm.

    Args:
        edges (List[Tuple[int, int, int]]): List of edges with (u, v, weight).
        n (int): Number of vertices.

    Returns:
        Tuple[List[Tuple[int, int, int]], int]: Edges in the MST and total weight.
    """
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


# Main Function
def main() -> None:
    # Example 1: Activity Selection Problem
    activities = [
        (1, 4),
        (3, 5),
        (0, 6),
        (5, 7),
        (3, 8),
        (5, 9),
        (6, 10),
        (8, 11),
        (8, 12),
        (2, 13),
        (12, 14),
    ]
    print("Activity Selection:", activity_selection(activities))

    # Example 2: Job Scheduling Problem
    tasks = [(2, 25), (1, 20), (2, 15), (1, 10)]
    max_deadline = 2
    print("Job Scheduling:", job_scheduling(tasks, max_deadline))

    # Example 3: Prim's Algorithm
    graph = {
        0: [(1, 10), (2, 6), (3, 5)],
        1: [(0, 10), (3, 15)],
        2: [(0, 6), (3, 4)],
        3: [(0, 5), (1, 15), (2, 4)],
    }
    print("Prim's MST:", prim(graph, 0))

    # Example 4: Kruskal's Algorithm
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    print("Kruskal's MST:", kruskal(edges, 4))


if __name__ == "__main__":
    main()
