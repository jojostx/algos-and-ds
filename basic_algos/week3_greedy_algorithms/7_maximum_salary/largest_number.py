from functools import cmp_to_key


def sort_custom(a, b):
    if int(a+b) > int(b+a):
        return -1
    elif int(a+b) < int(b+a):
        return 1
    else:
        return 0


def largest_number(numbers):
    numbers = list(map(str, numbers))

    return "".join(sorted(numbers, key=cmp_to_key(sort_custom)))


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))
