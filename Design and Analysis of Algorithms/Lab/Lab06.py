def binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        j = min(i, k)
        while j > 0:
            dp[j] = dp[j] + dp[j - 1]
            j -= 1
    return dp[k]


def coin_row(coins):
    n = len(coins)
    dp = [0] * (n + 1)
    dp[1] = coins[0]
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + coins[i - 1])
    return dp[n]


def change_making(coins, amount):
    n = len(coins)
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1


def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


def main():
    print(binomial_coefficient(5, 2))  # 10
    print(coin_row([5, 1, 2, 10, 6, 2]))  # 17
    print(change_making([1, 2, 5], 11))  # 3
    print(knapsack([10, 20, 30], [60, 100, 120], 50))  # 220


if __name__ == "__main__":
    main()
