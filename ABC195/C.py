import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N = input()

div = "999"
ans = 0
while len(N) > len(div):
    ans += int(N) - int(div)
    div += "999"
print(ans)