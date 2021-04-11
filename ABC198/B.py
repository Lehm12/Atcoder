import math
import itertools
#import numpy as np
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n = input()
count = 0
for i in range(1,len(n)+1):
    if n[-i] == "0":
        count += 1
    else:
        break
length = len(n)-count
for i in range(int(length/2)):
    if n[i] != n[length-1-i]:
        print("No")
        exit(0)
print("Yes")