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
#mou = LLI(n)
name = []
high = []
for i in range(n):
    a,b = map(str, input().split())
    name.append(a)
    high.append(int(b))

temp = sorted(high)
k = temp[-2]

for i in range(n):
    if high[i] == k:break
print(name[i])