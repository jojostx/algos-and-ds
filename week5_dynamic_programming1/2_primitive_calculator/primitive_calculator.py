def compute_operations(n):
    dp = [0] * (n + 1)
    parent = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        parent[i] = i - 1

        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            parent[i] = i // 2

        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            parent[i] = i // 3

    sequence = []
    x = n
    while x > 0:
        sequence.append(x)
        x = parent[x]
    sequence.reverse()

    return sequence


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
