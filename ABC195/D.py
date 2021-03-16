import math
import itertools
import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N,M,Q = MI()
w = LLI(N)
w = sorted(w, key=lambda x:x[1], reverse=True)
x = LI()

for _ in range(Q):
    ans = 0
    L,R = MI()
    box = x[:L-1] + x[R:]
    box.sort()
    temp = box
    for i in range(N):
        for j in range(len(temp)):
            if w[i][0] <= temp[j]:
                ans += w[i][1]
                temp.pop(j)
                break
    print(ans)