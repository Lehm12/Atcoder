import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N = I()
minn=10**5+1
a_min=10**5+1
b_min=10**5+1
la = []
lb = []
for i in range(N):
    a,b = MI()
    if minn > a+b:
        minn = a+b
    la.append(a)
    lb.append(b)
yu = 10**5+1
for i in range(N):
  for j in range(i+1,N):
    temp = max(la[i],lb[j])
    if yu > temp:
      yu = temp
for i in range(N):
  for j in range(i+1,N):
    temp = max(la[j],lb[i])
    if yu > temp:
      yu = temp
print(min(minn, yu))