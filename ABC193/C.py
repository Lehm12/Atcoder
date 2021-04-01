import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N = I()
count = N

b = []
for i in range(2,int(math.sqrt(N))+1):
    flag = 0
    zyou = 2
    while flag == 0:
        if i ** zyou <= N:
            b.append(i**zyou)
            zyou += 1
        else:
            zyou -= 1
            flag = 1
b = set(b)
print(N - len(b))