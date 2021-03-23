import math
import itertools
import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
def LLS(n): return [list(map(str, input().split())) for _ in range(n)]

N = I()
C = []
sikii = 10**9+1
min = []
for i in range(N):
    c = LI()
    C.append(c)
    if sikii > c[0]:
        sikii = c[0]
        min = []
        min.append(i)
    elif sikii == c[0]:
        min.append(i)
syou = C[min[0]]

for i in range(len(min)-1):
    for j in range(1,N):
        if syou[j] - C[min[i]][j] > 0:
            syou = C[min[i]]
B = syou
flag = 0
A = []
for i in range(N):
    sa = C[i][0] - B[0]
    for j in range(1,N):
        if C[i][j] - B[j] != sa:
            flag = 1
            break
    if flag == 1:
        break
    else:
        A.append(sa)
if flag == 0:
    print("Yes")
    print(*A)
    print(*B)
else:
    print("No")
