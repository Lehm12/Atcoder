import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

x = input()
flag = 0
for i in range(len(x)):
    if x[i] == ".":
        ans = x[:i]
        flag = 1
        break
if flag == 0:
    ans = x
print(ans)
