import math
import sys
import itertools
#import numpy as np
from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 5)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

s = input()

count = 0
for i in range(len(s)-3):
    if s[i] == 'Z':
        if s[i:i+4] == 'ZONe':
            count += 1
print(count)