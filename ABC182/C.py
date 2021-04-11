import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n = input()
keta = len(n)
N = int(n)
ans = mod
for i in range(2**(keta)):
    num = ""
    count = 0
    for j in range(keta):
        if (i>>j) & 1 == 1:
            count += 1
            num += n[j]
    if len(num) != 0:
        if int(num)%3 == 0:
            ans = min(ans, keta-count)
if ans == mod:
    print(-1)
else:
    print(ans)
