import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

a,b,w = MI()

m = 10**100
ma = 0
for i in range(1,10**6+1):
    c = a * i
    d = b * i
    if c <= w*1000 and w*1000 <= d:
        m = min(i,m)
        ma = max(i,ma)

if ma != 0:
    print(m,ma)
else:
    print("UNSATISFIABLE")