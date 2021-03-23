import math
from functools import reduce
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N, K = map(str,input().split())
K = int(K)

a = N
past_a = -1
for i in range(K):
    a = list(a)
    a = [int(b) for b in a]
    temp1 = sorted(a, reverse=True)
    temp2 = sorted(a)
    temp1 = int(reduce(lambda x, y: x + y, [str(x) for x in temp1]))
    temp2 = int(reduce(lambda x, y: x + y, [str(x) for x in temp2]))
    a = temp1 -temp2
    a = str(a)
print(a)

