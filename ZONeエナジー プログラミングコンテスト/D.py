import math
import itertools
from collections import deque
import sys
#import numpy as np
from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 5)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

S = input()
T = deque()
flag = True

count = 0
for i in range(len(S)):
    if S[i] == 'R':
        flag = not flag
    elif len(T) != 0:
        if not flag:
            if S[i] == T[-1]:
                T.pop()
            else:
                T.append(S[i])
        else:
            if S[i] == T[0]:
                T.popleft()
            else:
                T.appendleft(S[i])
    else:
        T.append(S[i])
if flag:
    T.reverse()
print(*T, sep='')

