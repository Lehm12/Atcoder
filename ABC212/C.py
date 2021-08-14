#import math
import itertools
from collections import deque, Counter, defaultdict
import sys
import copy
#import numpy as np
#from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
#G = [[] for _in range(n)]

n, m = MI()
a = sorted(LI())
b = sorted(LI())

if a[n-1] < b[0]:
    print(b[0]-a[n-1])
    exit()
if a[0] > b[m-1]:
    print(a[0] - b[m-1])
    exit()

i = 0
j = 0
ans = 100000
while True:
    ans = min(ans, abs(a[i]-b[j]))
    if a[i] < b[j]:
        i += 1
        if i == n:
            break
    else:
        j += 1
        if j == m:
            break
    if ans == 0:
        print(ans)
        exit()
print(ans)




