import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N = I()
a = LI()
ans = 10**18

for i in range(2**(N-1)):
    flag = 0
    o = 0
    x = 0
    for j in range(N):
        o = o | a[j]
        if (i>>j) & 1 == 1:
            if flag == 0:
                x = o
                o = 0
                flag = 1
            else:
                x = x ^ o
                o = 0
    x = x ^ o
    ans = min(ans,x)

print(ans)


