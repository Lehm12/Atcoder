import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

v,t,s,d = MI()

min = v*t
max = v*s

if min <= d and max >= d:
    print("No")
else:
    print("Yes")