import math
import itertools
from collections import deque
import sys
#import numpy as np
from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 5)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n, k = MI()

for i in range(k):
    if n % 200 == 0:
        n = int(n/200)
    else:
        n = int(str(n)+"200")
print(n)
