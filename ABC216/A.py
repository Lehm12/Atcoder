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

s = input()
x = ''

for i in range(len(s)):
    if s[i] == ".":
        y = int(s[i+1])
        break
    else:
        x += str(s[i])

if y <= 2:
    y = '-'
elif y <= 6:
    y = ''
else:
    y = '+'
print(x+y)