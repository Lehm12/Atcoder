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

x = input()
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])

if a == b and b == c and c == d:
    print("Weak")
    exit()

if a == 9:
    if b==0:
        if c == 1:
            if d == 2:
                print("Weak")
                exit()
elif a+1 == b:
    if b == 9:
        if c == 0:
            if d == 1:
                print("Weak")
                exit()
    elif b+1 == c:
        if c == 9:
            if d == 0:
                print("Weak")
                exit()
        elif c+1 == d:
            print("Weak")
            exit()

print("Strong")