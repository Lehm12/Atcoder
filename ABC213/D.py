#import math
import itertools
from collections import deque, Counter, defaultdict
import sys
#import numpy as np
#from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
# G = [[] for i in range(n)]

n = I()
load = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = MI()
    load[a].append(b)
    load[b].append(a)
for i in range(n+1):
    load[i].sort()


def dfs(now):
    candi = load[now]
    for i, c in enumerate(candi):
        if visit[c] == 0:
            visit[c] = 1
            #first[c] = now
            ans.append(c)
            #load[now].pop(i)
            dfs(c)
            ans.append(now)

pos = 1
ans = []
visit = [0]*(n+1)
visit[pos] = 1
ans. append(pos)
#first = [[] for i in range(n+1)]
dfs(pos)
print(*ans)