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

n = I()
s = input()
print(s)

for i in range(n):
    if s[i] == "1":
        if i % 2 == 0:
            print("Takahashi")
        else:
            print("Aoki")
        exit()

