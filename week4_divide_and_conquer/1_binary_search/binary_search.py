def binary_search(keys, query):
    start = 0
    end = len(keys) - 1

    while start <= end:
        mid = (start + end) // 2

        if query == keys[mid]:
            return True
        elif query < keys[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
