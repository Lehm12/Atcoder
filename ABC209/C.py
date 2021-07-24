#import math
import itertools
from collections import deque, Counter, defaultdict
import sys
import copy
#import numpy as np
#from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
#G = [[] for _in range(n)]

n = I()
c = LI()
c = sorted(c)
ans = c[0]
for i in range(1,n):
    ans = ans * max(c[i]-i, 0) % mod
print(ans)