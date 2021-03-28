import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(str, input())) for _ in range(n)]

h,w,x,y = MI()
s = LLI(h)

a = 0
for i in range(x-1):
    if s[x-2-i][y-1] == "#":
        break
    else:
        a += 1
b = 0
for i in range(h-x):
    if s[x+i][y-1] == "#":
        break
    else:
        b += 1
c = 0
for i in range(y-1):
    if s[x-1][y-2-i] == "#":
        break
    else:
        c += 1
d = 0
for i in range(w-y):
    if s[x-1][y+i] == "#":
        break
    else:
        d += 1
print(a+b+c+d+1)