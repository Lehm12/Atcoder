import math
import itertools
from collections import deque, Counter
import sys
#import numpy as np
from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 5)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n = I()
a = LI()
kane = 0
sum = 0
k = 1
max = a[0]
for i in range(1, n+1):
    ans = 0
    sum += a[i-1]
    ans += sum
    if max < a[i-1]:
        max = a[i-1]
    m = max
    ans += m * k
    ans += kane
    print(ans)

    k += 1
    ans -= m * k
    kane += sum

