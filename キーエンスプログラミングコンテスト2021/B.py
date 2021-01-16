import itertools
import numpy as np
import collections
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N,K = MI()

a = LI()
a = sorted(a)
max = max(a)

count = [0]*(max+1)
for i in a:
  count[i] += 1

ans = 0
zyougen = K
for i in range(len(count)):
  zyougen = min(zyougen, count[i])
  ans += zyougen

print(ans)