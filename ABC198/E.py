import math
import itertools
import sys
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

sys.setrecursionlimit(10 ** 5)

n = I()
c = LI()
hen = [[] for _ in range(n)]

for i in range(n-1):
    a, b = MI()
    hen[a-1].append(b)
    hen[b-1].append(a)

ans = []
color = [0]*(10**5+5)
pos = 1
visit = [0]*n

def dfs(pos):
    if color[c[pos-1]-1] == 0:
        ans.append(pos)
    color[c[pos-1]-1] += 1
    visit[pos-1] = 1
    for i in hen[pos-1]:
        if visit[i-1] == 0:
            dfs(i)
    color[c[pos-1]-1] -= 1

dfs(pos)
ans.sort()
for i in ans:
    print(i)