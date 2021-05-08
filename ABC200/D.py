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
aa = np.array(a)
aa = aa % 200
aa = list(aa)

c = []

for i in range(1,2**n+1):
    temp = 0
    ans = []
    for j in range(n):
        if (i >> j) & 1:
            temp += a[j]
            ans.append(j+1)
    if aa.count(temp%200) > 0 and len(ans) > 0:
        if len(ans) > 1:
            print("Yes")
            print(1, aa.index(temp%200)+1)
            print(len(ans), *ans)
            exit(0)
        elif ans[0] != aa.index(temp%200)+1:
            print("Yes")
            print(1, aa.index(temp%200)+1)
            print(len(ans), *ans)
            exit(0)

print("No")
