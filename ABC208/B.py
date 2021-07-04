#import math
import itertools
from collections import deque, Counter, defaultdict
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

b = I()

coin = []

temp = 1
for i in range(1,11):
    temp = temp * i
    coin.append(temp)

for i in range(10):
    if coin[i] > b:
        break
ans =0
while True:
    ans += int(b/coin[i])
    b -= int(b/coin[i]) * coin[i]
    i -= 1
    if b == 0:
        break
print(ans)