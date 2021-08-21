
#import math
import itertools
from collections import deque, Counter, defaultdict
import sys
import copy
#import numpy as np
#from decimal import Decimal
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
#G = [[] for _in range(n)]

s, k = map(str, input().split())
k = int(k)

candi = list(itertools.permutations(s))
candi = list(set(candi))
chara = []
for i in candi:
    temp = ""
    for j in range(len(i)):
        temp += i[j]
    chara.append(temp)
chara = sorted(chara)
print(chara[k-1])
