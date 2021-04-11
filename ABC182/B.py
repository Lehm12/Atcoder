import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n = I()
a = LI()

big = 0
ans = 0
for i in range(2, max(a)+1):
    count = 0
    for j in range(n):
        if a[j] % i == 0:
            count += 1
    if big <= count:
        ans = i
        big = count

print(ans)