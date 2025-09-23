# maximum_gold_knapsack.py
def maximum_gold(capacity, weights):
    """
    0/1 knapsack where item value == item weight.
    Returns maximum total weight (value) that fits into capacity.
    """
    if capacity <= 0 or not weights:
        return 0

    dp = [0] * (capacity + 1)
    for w in weights:
        if w > capacity:
            continue
        for c in range(capacity, w - 1, -1):
            candidate = dp[c - w] + w
            if candidate > dp[c]:
                dp[c] = candidate
    return dp[capacity]


if __name__ == '__main__':
    # Read first non-empty line (expects: "<capacity> <n>")
    while True:
        first = input().strip()
        if first:
            break
    parts = list(map(int, first.split()))
    if len(parts) >= 2:
        capacity, n = parts[0], parts[1]
        weights = parts[2:]  # maybe some weights are on the same line
    else:
        # If first line had only capacity, read next non-empty line for n (unlikely for this problem but robust)
        capacity = parts[0]
        while True:
            second = input().strip()
            if second:
                break
        sec_parts = list(map(int, second.split()))
        n = sec_parts[0]
        weights = sec_parts[1:]

    # Continue reading lines until we have n weights
    while len(weights) < n:
        line = input().strip()
        if not line:
            continue
        weights.extend(map(int, line.split()))

    weights = weights[:n]
    print(maximum_gold(capacity, weights))
