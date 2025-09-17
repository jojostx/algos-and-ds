# robust_partition3.py
from sys import stdin

def partition3(values):
    total = sum(values)
    if total % 3 != 0:
        return 0
    target = total // 3

    # quick rejection
    values.sort(reverse=True)
    if values and values[0] > target:
        return 0

    reachable = {(0, 0)}
    prefix = 0

    for val in values:
        next_reachable = set()
        for a, b in reachable:
            # put val into A
            if a + val <= target:
                next_reachable.add((a + val, b))
            # put val into B
            if b + val <= target:
                next_reachable.add((a, b + val))
            # put val into C (implicit): check capacity
            c = prefix - a - b
            if c + val <= target:
                next_reachable.add((a, b))
        prefix += val
        if not next_reachable:
            return 0
        reachable = next_reachable

    return 1 if (target, target) in reachable else 0

if __name__ == '__main__':
    try:
        n = int(input().strip())
    except EOFError:
        raise SystemExit("No input provided")
    vals = []
    # keep reading until we have n numbers (supports values across multiple lines)
    while len(vals) < n:
        line = input().strip()
        if not line:
            continue
        vals.extend(map(int, line.split()))
    vals = vals[:n]
    print(partition3(vals))
