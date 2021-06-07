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
t = LI()
t = sorted(t, reverse=True)
s = sum(t)

dp = [[0]*(s+1) for i in range(n+1)] #dp[i][j] i番目までの数の部分和でjは作れるか
ans = 0

for i in range(n):
    dp[i][0] = 1

for i in range(n):
    for k in range(s+1):
        if k - t[i] >= 0:
            dp[i+1][k] = dp[i][k] | dp[i][k-t[i]]
        else:
            dp[i+1][k] = dp[i+1][k] | dp[i][k]

for k in range(int(-(-s//2)),s+1):
    if dp[n][k] == 1:
        print(k)
        exit()
