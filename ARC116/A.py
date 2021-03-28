import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
def LLS(n): return [list(map(str, input().split())) for _ in range(n)]

T = I()

for i in range(T):
    test = I()
    if test % 4 == 0:
        print("Even")
    elif test % 2 == 0:
        print("Same")
    else:
        print("Odd")
