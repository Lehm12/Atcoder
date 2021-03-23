import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
def LLS(n): return [list(map(str, input().split())) for _ in range(n)]

N = I()

a = []
a.append(1)
for i in range(2,N+1):
    flag = 0
    for j in range(2,int(i/2)+1):
        if i/j == int(i/j):
            a.append(a[int(i/j)-1]+1)
            flag = 1
            break
    if flag == 0:
        a.append(2)
print(*a)