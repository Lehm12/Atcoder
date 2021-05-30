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
mura = 10**100 + 1

n,k = MI()
a = LLI(n)
a = sorted(a)
ans = 0
last = 0
kane = k
for i in range(n):
    kane -= a[i][0] - last
    ans += a[i][0] - last
    if kane < 0:
        print(ans + kane)
        exit()

    kane += a[i][1]
    last = a[i][0]

print(min(ans+kane,mura))