import math
import itertools
import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N = I()
B = LI()
A = np.array(B)
A = A.reshape(2,-1)
A = np.amax(A,axis=1)
ans_item = np.min(A)

for i in range(2**N):
  if B[i] == ans_item:
    print(i+1)


