import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n,x = MI()
A = LI()

ans = []
for i in range(n):
    if A[i] != x:
        ans.append(A[i])
if len(ans) != 0:
    print(*ans)
else:
    print(" ")