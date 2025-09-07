def CountInversions(arr, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2

    # Count inversions in left half
    inv_left = CountInversions(arr, left, mid)

    # Count inversions in right half
    inv_right = CountInversions(arr, mid + 1, right)

    # Count cross inversions while merging
    inv_merge = MergeAndCount(arr, left, mid, right)

    return inv_left + inv_right + inv_merge


def MergeAndCount(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            inv_count += (mid - i + 1)  


    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[left + k] = temp[k]

    return inv_count


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(CountInversions(elements, 0, input_n - 1))
