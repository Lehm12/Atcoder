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

a,b,c = MI()
if a == 0:
    a = 0.1
if b == 0:
    b = 0.1

def no(ans):
    if ans < 0:
        print("<")
    elif ans > 0:
        print(">")
    else:
        print("=")

if (a >= 0 and b >= 0) or (a < 0 and b < 0):
    no(a-b)
elif (a >= 0 and b < 0):
    if c%2 == 0:
        no(a-(-b))
    else:
        no(a)
else: # (a < 0 and b >= 0)
    if c%2 == 0:
        no((-a)-b)
    else:
        no(-b)
