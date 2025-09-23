def max_dot_product(a, b):
    a.sort(), b.sort()
    return sum(x*y for x, y in zip(a, b))

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
