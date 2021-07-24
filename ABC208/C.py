#import math
import itertools
from collections import deque, Counter, defaultdict
import sys
import numpy as np
from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
#G = [[] for _in range(n)]

n, k = MI()
a = np.array(LI())
index = np.argsort(a)

human = [0] * n

sum = int(Decimal(k)/Decimal(n))
k -= sum * n

temp = index[:k]

for i in temp:
    human[i] += 1
human = list(human)
for i in human:
    print(i+sum)