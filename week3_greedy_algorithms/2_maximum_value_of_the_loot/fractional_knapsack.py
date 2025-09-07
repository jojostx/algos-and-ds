from sys import stdin

def optimal_value(capacity, weights, values):
    value = 0.0
    # create list of (ratio, value, weight)
    items = [(v / w, v, w) for v, w in zip(values, weights)]
    # sort by ratio descending
    items.sort(reverse=True, key=lambda x: x[0])
    
    for ratio, v, w in items:
        if capacity == 0:
            break
        take_weight = min(w, capacity)  # take as much as fits
        value += take_weight * ratio
        capacity -= take_weight
    return value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
