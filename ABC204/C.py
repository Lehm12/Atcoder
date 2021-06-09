#import math
import itertools
from collections import deque, Counter
import sys
#import numpy as np
#from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 8)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
# G [[] for i in range(N)]

n,m = MI()
if m == 0:
    print(n)
    exit()

miti = LLI(m)
miti = sorted(miti)
load = [[] for i in range(n)]

for start, end in miti:
    load[start-1].append(end)

ans = 0
go = [0] * n

def dfs(pos):
    for end in load[pos-1]:
        if go[end-1] == 0:
            go[end-1] = 1
            dfs(end)

for i in range(n):
    go = [0] * n
    go[i] = 1
    dfs(i+1)
    ans += sum(go)
print(ans)