import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N = I()
ans = mod
for i in range(N):
    a,p,x = MI()
    if x-a > 0:
        ans = min(ans,p)
if ans == mod:
    print(-1)
else:
    print(ans)