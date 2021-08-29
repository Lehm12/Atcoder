
import math
import itertools
from collections import deque, Counter, defaultdict
import sys
#import numpy as np
#from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
#G = [[] for _in range(n)]

n = I()
s = []
t = []

for i in range(n):
    a, b = map(str, input().split())
    s.append(a)
    t.append(b)

ans = 'No'
for i in range(n-1):
    for j in range(i+1,n):
        if s[i] == s[j] and t[i] == t[j]:
            ans = 'Yes'
            break
print(ans)

