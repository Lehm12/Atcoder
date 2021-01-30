import math
import itertools

# import numpy as np
mod = 10 ** 9 + 7


def I(): return int(input())


def LI(): return list(map(int, input().split()))


def MI(): return map(int, input().split())


def LLI(n): return [list(map(int, input().split())) for _ in range(n)]


N, M = MI()
a = LLI(M)
K = I()
b = LLI(K)
ans = 0
for i in itertools.product(*b):
    ball = list(set(i))
    temp = 0
    for c, d in a:
        if c in ball and d in ball:
            temp += 1

    if temp > ans:
        ans = temp
print(ans)