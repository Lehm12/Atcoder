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

n = I()
a = LI()

ans = 0
for i in range(n):
    ans += max(0, a[i]-10)
print(ans)