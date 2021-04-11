import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

r, x, y = MI()

kyori = math.sqrt(x**2+y**2)
if kyori == r:
    print(1)
    exit(0)
elif kyori < 2*r:
    print(2)
    exit(0)
kyori = kyori/r
print(math.ceil(kyori))