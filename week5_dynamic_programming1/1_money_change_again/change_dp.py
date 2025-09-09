def change(money):
    coins = [1, 3, 4]
    dp = [float('inf')] * (money + 1)
    dp[0] = 0

    for x in range(1, money + 1):
        for c in coins:
            if x - c >= 0:
                dp[x] = min(dp[x], dp[x - c] + 1)

    return dp[money] if dp[money] != float('inf') else -1


if __name__ == '__main__':
    m = int(input())
    print(change(m))
