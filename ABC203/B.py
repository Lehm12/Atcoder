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

n, k = MI()

sum = 0
for i in range(1,n+1):
    temp = 1
    for j in range(k):
        sum += 100*i + temp
        temp += 1
print(sum)
