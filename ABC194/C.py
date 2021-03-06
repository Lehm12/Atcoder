import math
import itertools
import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N = I()
a = LI()
a = np.array(a)
a2 = a**2
sig = []
pai = []
temp1 = 0
temp2 = 0
for i in range(N):
    temp1 += a[i]
    sig.append(temp1)
    temp2 += a2[i]
    pai.append(temp2)

ans = 0
for i in range(1,N):
    ans += i*a2[i] - 2*a[i]*sig[i-1] + pai[i-1]
print(ans)