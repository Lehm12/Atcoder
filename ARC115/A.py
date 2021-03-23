import math
import itertools
import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
def LLS(n): return [list(map(str, input().split())) for _ in range(n)]

N,M = MI()
guu = 0
ki = 0
for i in range(N):
    s = list(input())
    for j in range(M):
        s[j] = int(s[j])
    su = sum(s)
    if su % 2 == 0:
        guu += 1
    else:
        ki += 1

print(guu * ki)