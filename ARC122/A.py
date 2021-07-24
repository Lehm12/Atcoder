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
#G = [[] for _in range(n)]

def fibonacci(n):
    return round((((1 + 5 ** 0.5) / 2) ** (n+1) - ((1 - 5 ** 0.5) / 2) ** (n+1)) / 5 ** 0.5)

n = I()
a = LI()
s = sum(a)

ans = 0
dp = [[0]*2 for _ in range(n)] #0:+, 1:-
dp[0][0] = 1

for i in range(1,n):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % mod
    dp[i][1] = dp[i-1][0] % mod

ans += s * (dp[n-1][0] + dp[n-1][1])
for i in range(1,n):
    ans -= a[i] * (dp[i][1] * dp[n-i-1][0]) * 2

print(ans%mod)