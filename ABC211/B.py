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
# G = [[] for i in range(n)]
s = []
for i in range(4):
    s.append(input())

if not "H" in s:
    print("No")
    exit()
if not "2B" in s:
    print("No")
    exit()
if not "3B" in s:
    print("No")
    exit()
if not "HR" in s:
    print("No")
    exit()

print("Yes")

