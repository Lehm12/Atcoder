import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

a,b,c = MI()

if c==0:
  if a > b:
    print("Takahashi")
  else:
    print("Aoki")
else:
  if b > a:
    print("Aoki")
  else:
    print("Takahashi")