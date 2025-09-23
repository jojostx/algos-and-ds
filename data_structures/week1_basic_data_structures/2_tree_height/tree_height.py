# python3

import sys
import threading


def compute_height(n, parents):
    children = [[] for _ in range(n)]
    root = None

    for i, p in enumerate(parents):
        if p == -1:
            root = i
        else:
            children[p].append(i)

    max_height = 0
    stack = [(root, 1)]
    
    while stack:
        node, depth = stack.pop()
        max_height = max(max_height, depth)
        for child in children[node]:
            stack.append((child, depth + 1))
 
    return max_height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
