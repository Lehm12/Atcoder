import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

a,b = MI()

if a < b:
  if a+3 > b:
    print("Yes")
  else:
    print("No")
else:
  if b+3 > a:
    print("Yes")
  else:
    print("No")