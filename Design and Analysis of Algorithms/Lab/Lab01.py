from math import pow


def main():
    print(Ex01(3))
    print(Ex02(2, 2))
    print(Ex03(3))
    print(Ex04(10))
    print(Ex05([1, 2, 3, 4, 4]))
    print(Ex06([1, 2, 7, 3, 4, 4]))
    print(
        Ex07([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    )  # Output: [[58, 64], [139, 154]]
    print(Ex08([[1, 2, 3], [4, 5, 6]], 2))
    print(
        Ex09(
            [[1, 2, 3], [4, 5, 6]],
            [[7, 8, 9], [10, 11, 12]],
        )
    )
    print(
        Ex10(
            [[1, 2, 3], [4, 5, 6]],
            [[7, 8, 9], [10, 11, 12]],
        )
    )


def Ex01(n):
    print()
    result = 0
    for i in range(2, n + 1):
        result += 1 / (1 - i**i)
    print("C(n) = n - 1")
    print("Worst case: O(n)")

    return result


def Ex02(m, n):
    print()
    result = 0
    for i in range(1, n + 1):
        result += pow(-1, i + 1) * 1 / (1 + pow(m, i))
    print("C(n) = n")
    print("Worst case: O(n)")

    return result


def Ex03(n):
    print()
    result = 0
    for i in range(1, n + 1):
        result += pow(i, 3)

    print("C(n) = n")
    print("Worst case: O(n)")
    return result


def Ex04(n):
    print()
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("C(n) = n - 1")
    print("Worst case: O(n)")

    return result


def Ex05(arr):
    print()
    addedElement = set()

    for element in arr:
        if element in addedElement:
            return False
        addedElement.add(element)

    print("C(n) = n")
    print("Worst case: O(n)")

    return True


def Ex06(arr):
    print()
    maxNumber = arr[0]

    for element in arr:
        if element > maxNumber:
            maxNumber = element

    print("C(n) = n - 1")
    print("Worst case: O(n)")

    return maxNumber


def Ex07(matrixA, matrixB):
    print()
    rowsA = len(matrixA)
    columnsA_rowsB = len(matrixA[0])
    columnsB = len(matrixB[0])

    matrixC = [[0] * columnsB for _ in range(rowsA)]

    for i in range(rowsA):
        for j in range(columnsB):
            matrixC[i][j] = sum(
                matrixA[i][k] * matrixB[k][j] for k in range(columnsA_rowsB)
            )

    print("C(n) = n^3")
    print("Worst case: O(n^3)")

    return matrixC


def Ex08(matrix, k):
    print()
    rows = len(matrix)
    columns = len(matrix[0])

    matrixResult = [[0] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            matrixResult[i][j] = matrix[i][j] * k

    print("C(n) = n^2")
    print("Worst case: O(n^2)")

    return matrixResult


def Ex09(matrixA, matrixB):
    print()
    rowsA = len(matrixA)
    columnsA_rowsB = len(matrixA[0])
    columnsB = len(matrixB[0])

    matrixC = [[0] * columnsB for _ in range(rowsA)]

    for i in range(rowsA):
        for j in range(columnsA_rowsB):
            matrixC[i][j] = matrixA[i][j] - matrixB[i][j]

    print("C(n) = n^2")
    print("Worst case: O(n^2)")

    return matrixC


def Ex10(matrixA, matrixB):
    print()
    rowsA = len(matrixA)
    columnsA_rowsB = len(matrixA[0])
    columnsB = len(matrixB[0])

    matrixC = [[0] * columnsB for _ in range(rowsA)]

    for i in range(rowsA):
        for j in range(columnsA_rowsB):
            matrixC[i][j] = matrixA[i][j] + matrixB[i][j]

    print("C(n) = n^2")
    print("Worst case: O(n^2)")

    return matrixC


if __name__ == "__main__":
    main()
