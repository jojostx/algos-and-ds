def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(i, j, ops, m, M):
    min_val = float('inf')
    max_val = float('-inf')
    
    for k in range(i, j):
        op = ops[k]
        a = evaluate(M[i][k], M[k+1][j], op)
        b = evaluate(M[i][k], m[k+1][j], op)
        c = evaluate(m[i][k], M[k+1][j], op)
        d = evaluate(m[i][k], m[k+1][j], op)
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)

    return min_val, max_val

def maximum_value(expr):
    digits = [int(expr[i]) for i in range(0, len(expr), 2)]
    ops = [expr[i] for i in range(1, len(expr), 2)]
    n = len(digits)

    m = [[0] * n for _ in range(n)]  # min values
    M = [[0] * n for _ in range(n)]  # max values

    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]

    for s in range(1, n):  # subexpression length
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, ops, m, M)

    return M[0][n-1]


if __name__ == "__main__":
    print(maximum_value(input()))
