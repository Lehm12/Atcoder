import math
import itertools
from collections import deque, Counter
import sys
#import numpy as np
from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 5)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n,k = MI()
index = k**2//2+1

a = LLI(n)
s = [[0]*(n+1) for _ in range(n+1)]

ng = -1
ok = max(max(a))

while ng + 1 != ok:
    mid = (ng+ok)//2
    for i in range(n):
        for j in range(n):
            s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j]
            if a[i][j] > mid:
                s[i+1][j+1] += 1
    ext = False
    for i in range(n-k+1):
        for j in range(n-k+1):
            if s[i+k][j+k] + s[i][j] - s[i][j+k] - s[i+k][j] < index:
                ext = True

    if ext:
        ok = mid
    else:
        ng = mid

print(ok)

