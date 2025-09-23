def gcd(a, b):
    if b == 0:
        return a
    
    b_ = b
    b = a % b
    a = b_
    return gcd(a, b)

def lcm(a, b):
    return int((a * b)/gcd(a, b))


if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    print(lcm(a, b))
