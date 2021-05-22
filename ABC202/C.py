import math
import itertools
from collections import deque, Counter
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
a = Counter(LI())
b = LI()
c = Counter(LI())
ans = 0
index = []
num = []
for i in range(len(b)):
    if a[b[i]] != 0:
        index.append(i+1)
        num.append(a[b[i]])

for i in range(len(index)):
    if c[index[i]] != 0:
        ans += num[i] * c[index[i]]
print(ans)