import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n,s,d = MI()

ans = 0
for i in range(n):
  x,y = MI()
  if x < s and y > d:
    ans += y
if ans == 0:
  print("No")
else:
  print("Yes")