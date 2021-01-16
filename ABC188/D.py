import math
import itertools
import numpy as np

mod = 10 ** 9 + 7


def I(): return int(input())


def LI(): return list(map(int, input().split()))


def MI(): return map(int, input().split())


def LLI(n): return [list(map(int, input().split())) for _ in range(n)]


N, C = MI()
event = []
for i in range(N):
    a, b, c = MI()
    event.append((a - 1, c))
    event.append((b, -c))

event = sorted(event)
t = 0
fee = 0
ans = 0
for day, money in event:
    if day != t:
        ans += min(C, fee) * (day - t)
        t = day
    fee += money
print(ans)

