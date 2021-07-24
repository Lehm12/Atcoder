#import math
import itertools
from collections import deque, Counter
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
a = LI()
temp = len(set(a))
num = {}
for i in range(n):
    if num.get(str(a[i])) == None:
        num[str(a[i])] = 1
    else:
        num[str(a[i])] += 1
sum = n
ans = 0
for i in range(n):
    num[str(a[i])] -= 1
    n -= 1
    ans += (n - num[str(a[i])])
print(ans)