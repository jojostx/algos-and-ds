def edit_distance(s1, s2):
    n, m = len(s1), len(s2)
    # DP table, size (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base cases: empty string edits
    for i in range(n + 1):
        dp[i][0] = i  # deleting i chars
    for j in range(m + 1):
        dp[0][j] = j  # inserting j chars

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # deletion
                dp[i][j - 1] + 1,      # insertion
                dp[i - 1][j - 1] + cost  # substitution (or match if cost=0)
            )

    return dp[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
