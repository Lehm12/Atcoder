import math
import itertools
# import numpy as np
mod = 10 ** 9 + 7
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]


N = I()
n = str(N)
if len(n) == 1:
    print(0)
    exit(0)
if len(n) % 2 == 1:
    a = ""
    for i in range(len(n) - 1):
        a += "9"
    N = int(a)
    n = str(N)

a = n[:int(len(n) / 2)]
b = n[int(len(n) / 2):]

if int(a) <= int(b):
        print(int(a))
else:
        print(int(a)-1)

