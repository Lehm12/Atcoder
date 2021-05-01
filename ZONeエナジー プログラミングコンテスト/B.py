import math
import itertools
import sys
#import numpy as np
from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 5)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n, D, H = MI()

ans = 0

for i in range(n):
    d, h = MI()
    b = H - (H-h)/(D-d) * D
    ans = max(ans,b)
print(ans)
