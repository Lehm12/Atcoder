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

n = I()
s = LI()
t = LI()

get_time = [0] * n
m = 10**9
min_index = 0
for i in range(n):
    if m > t[i]:
        m = t[i]
        min_index = i

get_time[min_index] = m
T = m
index = min_index

for i in range(n-1):
    if index + 1 > n-1:
        get_time[0] = min(t[0], T + s[index])
        T = get_time[0]
        index = 0
    else:
        get_time[index+1] = min(t[index+1], T + s[index])
        T = get_time[index+1]
        index += 1

for i in get_time:
    print(i)