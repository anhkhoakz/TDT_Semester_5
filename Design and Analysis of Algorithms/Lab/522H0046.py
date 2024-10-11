import math
import itertools
import matplotlib.pyplot as plt


def Ex_A(a, n):
    if n == 0:
        return 1
    return a * Ex_A(a, n - 1)


def Ex_B(n, k):
    if k == 0 or k == n:
        return 1
    return Ex_B(n - 1, k - 1) + Ex_B(n - 1, k)


def Ex_C(matrix1, matrix2):
    n = len(matrix1)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        result.append(row)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def squared_distance(point1, point2):
    return sum((x - y) ** 2 for x, y in zip(point1, point2))


def nearest_pair(points):
    n = len(points)
    if n < 2:
        return None

    min_dist = float("inf")
    closest_pair = None

    for i in range(n):
        for j in range(i + 1, n):
            dist = squared_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])

    return closest_pair, math.sqrt(min_dist)


def calculate_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour)):
        total_distance += distance_matrix[tour[i]][tour[(i + 1) % len(tour)]]
    return total_distance


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def convex_hull(points):
    n = len(points)
    if n < 3:
        return points

    hull = set()

    for i in range(n):
        for j in range(i + 1, n):
            pos_side = neg_side = False

            for k in range(n):
                if k != i and k != j:
                    o = orientation(points[i], points[j], points[k])
                    if o == 1:
                        pos_side = True
                    elif o == 2:
                        neg_side = True
                    if pos_side and neg_side:
                        break

            if not (pos_side and neg_side):
                hull.add(points[i])
                hull.add(points[j])

    return list(hull)


def Ex_E(points):
    hull = convex_hull(points)

    print("Convex Hull points:", hull)

    plt.figure()
    plt.scatter(*zip(*points), color="blue", label="Points")
    plt.scatter(*zip(*hull), color="red", label="Convex Hull", marker="x")

    hull_points = sorted(hull, key=lambda p: (p[0], p[1]))
    for i in range(len(hull_points)):
        j = (i + 1) % len(hull_points)
        plt.plot(
            [hull_points[i][0], hull_points[j][0]],
            [hull_points[i][1], hull_points[j][1]],
            color="red",
        )

    plt.title("Convex Hull")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid()
    plt.show()


def Ex_F(distance_matrix):
    # traveling_salesman_brute_force
    n = len(distance_matrix)
    if n == 0:
        return None, 0

    cities = list(range(n))
    min_distance = float("inf")
    best_tour = None

    for perm in itertools.permutations(cities):
        current_distance = calculate_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = perm

    return best_tour, min_distance


def calculate_weight_value(subset, weights, values):
    total_weight = sum(weights[i] for i in subset)
    total_value = sum(values[i] for i in subset)
    return total_weight, total_value


def Ex_G(weights, values, max_weight):
    # knapsack_brute_force
    n = len(weights)
    best_value = 0
    best_subset = None

    for r in range(n + 1):
        for subset in itertools.combinations(range(n), r):
            total_weight, total_value = calculate_weight_value(subset, weights, values)

            if total_weight <= max_weight and total_value > best_value:
                best_value = total_value
                best_subset = subset

    return best_subset, best_value


def main():
    # Ex A
    print("Ex_A (2^3):", Ex_A(2, 3))

    # Ex B
    print("Ex_B (C(5, 2)):", Ex_B(5, 2))

    # Ex C
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    print("Ex01_C (matrix multiplication):")
    result = Ex_C(matrix1, matrix2)
    for row in result:
        print(row)

    # Ex D
    points = [[0, 3], [2, 3], [1, 1], [2, 1], [3, 0], [0, 0], [3, 3]]
    result = nearest_pair(points)
    print("Nearest pair of points:", result[0])
    print("Distance between them:", result[1])

    # Ex E

    points = [(0, 3), (2, 3), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
    Ex_E(points)

    # Ex F
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    best_tour, min_distance = Ex_F(distance_matrix)
    print("Best tour:", best_tour)
    print("Minimum distance:", min_distance)

    # Ex G
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 8]
    max_weight = 5

    best_subset, best_value = Ex_G(weights, values, max_weight)
    print("Best subset of items:", best_subset)
    print("Maximum value:", best_value)


if __name__ == "__main__":
    main()
