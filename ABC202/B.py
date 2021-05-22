import math
import itertools
from collections import deque
import sys
import numpy as np
from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 5)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

s = input()
ans = []
for i in range(len(s)):
    if s[-1-i] == "6":
        ans.append("9")
    elif s[-1-i] == "9":
        ans.append("6")
    else:
        ans.append(s[-1-i])
print(*ans, sep="")