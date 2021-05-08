import math
import itertools
from collections import deque
import sys
import numpy as np
from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 5)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n = I()
a = LI()
a = np.array(a)
a = a % 200
ans = 0
a = list(a)
temp = set(a)
for i in temp:
    num = a.count(i)
    ans += int(num*(num-1)/2)

print(ans)