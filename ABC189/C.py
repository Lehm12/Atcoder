#import math
#import itertools
#import numpy as np
#mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N = I()
a = LI()
max = 0
for i in range(N):
  m = a[i]
  if max < m:
    max = m
  for j in range(i+1,N):
    m = min(m, a[j])
    count = m * (j-i+1)
    if max < count:
      max = count
print(max)