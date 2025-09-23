def majority_element(elements):
    candidate = 0
    count = 0

    for num in elements:
        if count == 0:
            candidate = num
            count += 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    count = 0
    for num in elements:
        if num == candidate:
            count += 1
    
    if count > len(elements)/2:
        return 1

    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
