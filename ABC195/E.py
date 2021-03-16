import math
import itertools
import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N = I()
S = input()
X = input()
dp = []
dp.append([0])

for i in range(N):
    x = X[N-1-i]
    s = int(S[N-1-i])
    temp = []
    if x == "T":
        for j in range(7):
            if 10*j % 7 in dp[i] or (10*j+s) % 7 in dp[i]:
                temp.append(j)
    else:
        for j in range(7):
            if 10*j % 7 in dp[i] and (10*j+s) % 7 in dp[i]:
                temp.append(j)

    dp.append(temp)
if 0 in dp[N]:
    print("Takahashi")
else:
    print("Aoki")