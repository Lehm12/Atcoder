import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

a,b = MI()
a = a+b
if a >= 15 and b >= 8:
  print(1)
elif a>=10 and b>= 3:
  print(2)
elif a >= 3:
  print(3)
else:
  print(4)