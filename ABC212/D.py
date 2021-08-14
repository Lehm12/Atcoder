#import math
import itertools
import heapq
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

q = I()
ans = []
heapq.heapify(ans)
sum = 0
for i in range(q):
    a = LI()
    if len(a) == 1:
        print(heapq.heappop(ans)+sum)
    else:
        if a[0] == 1:
            heapq.heappush(ans, a[1]-sum)
        else:
            sum += a[1]
