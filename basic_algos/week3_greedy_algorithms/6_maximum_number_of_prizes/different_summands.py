def optimal_summands(n):
    summands = []
    current = 1
    while n > 0:
        if n - current > current:
            summands.append(current)
            n -= current
            current += 1
        else:
            summands.append(n)
            break
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
