import math
import itertools
from collections import deque, Counter
import sys
#import numpy as np
from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 5)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

a,b,c = MI()

if a == b:
    print(c)
elif b == c:
    print(a)
elif a == c:
    print(b)
else:
    print(0)