import math
import itertools
import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N = I()
a = LI()
b = LI()
a = np.array(a)
b = np.array(b)

ans = np.dot(a,b)

if ans == 0:
  print("Yes")
else:
  print("No")