import math

# import itertools
# import numpy as np
mod = 10 ** 9 + 7


def I(): return int(input())


def LI(): return list(map(int, input().split()))


def MI(): return map(int, input().split())


def LLI(n): return [list(map(int, input().split())) for _ in range(n)]


N, X = MI()
count = 0
X = X * 100
for i in range(N):
    v, p = MI()
    count += 1
    X -= v * p
    if X < 0:
        print(count)
        exit(0)
print("-1")
