import math
#import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N,M = MI()
A = LI()

count = [0]*N
minn = N
for i in range(M):
    count[A[i]] += 1
for i in range(N-M+1):
  if i == 0:
      for j in range(N):
          if count[j] == 0:
            if minn > j:
              minn = j
              break
  else:
      count[A[i-1]] -= 1
      count[A[i+M-1]] += 1
      if count[A[i-1]] == 0:
          minn = min(minn, A[i-1])
print(minn)