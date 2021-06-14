#import math
import itertools
from collections import deque, Counter
import sys
#import numpy as np
#from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
#G = [[] for _in range(n)]

n, q = MI()
a = sorted(LI())
m = max(a)
c = []
temp = 0
past = 0
for i in range(n):
    c.append(a[i]-temp-1+past)
    past += a[i]-temp-1
    temp = a[i]

for i in range(q):
    k = I()
    if k > c[-1]:
        print(k + n)
    else:
        ng = -1
        ok = n

        while ng + 1 != ok:
            mid = (ng + ok) // 2
            if k > c[mid]:
                ng = mid
            else:
                ok = mid
        print((a[ok]-1) - (c[ok]-k))