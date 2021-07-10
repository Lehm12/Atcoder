#import math
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

n,x = MI()
a = LI()
ans = sum(a)
ans -= int(n/2)

if ans <= x:
    print("Yes")
else:
    print("No")