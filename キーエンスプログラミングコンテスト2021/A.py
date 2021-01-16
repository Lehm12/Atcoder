import itertools
import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N = I()

a = LI()
b = LI()

a_max = 0
a_temp = []

for i in range(N):
    if a_max < a[i]:
        a_max = a[i]
        a_index = i

    a_temp.append(a_max)
max = 0
for i in range(N):
    if max < b[i]*a_temp[i]:
        max = b[i]*a_temp[i]
    print(max)