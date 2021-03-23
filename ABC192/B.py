import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

S = input()
flag = 0
for i in range(len(S)):
    s = S[i]
    if (i+1) % 2 == 0:
        if not s.islower():
            flag = 1
        else:
            flag = 0
            break
    else:
        if s.islower():
            flag = 1
        else:
            flag = 0
            break
if flag == 0:
    print("No")
else:
    print("Yes")