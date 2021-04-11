import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n = I()
a = LI()
ans = -10**8-1

pos = 0
past = 0
sa = 0
idou = 0
for i in range(n):
    pos += idou
    ans = max(ans, pos)
    pos += sa - idou
    pos += a[i]
    sa = pos - past
    idou = max(idou, sa)
    ans = max(ans, pos)
    past = pos
print(ans)



