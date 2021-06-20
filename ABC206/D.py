#import math
import itertools
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

class UnionFind():
    def __init__(self, n):
        self.n = n
        """
        親要素のノード番号を格納。
        要素が根(ルート)の場合は -(そのグループの要素数)　を格納する
        初期状態は１個なので -1 を格納
        """
        self.par = [-1] * (n + 1)

    def find(self, x):
        """
        要素xが所属するグループの根を返す。ついでに経路圧縮も
        """

        if self.par[x] < 0:
            return x
        # 根でないなら、親の要素で再検索
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same(self, x, y):
        """
        要素x,yが同じグループか判定
        """
        return self.find(x) == self.find(y)

    def union(self, x, y):
        """
        要素x,yのグループを併合する
        """
        # 根を探す
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        """
        要素xが属するグループのサイズを返す
        """

        return -self.par[self.find(x)]

    def members(self, x):
        """
        要素xが属するグループに属する要素をリストで返す
        """

        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """
        全ての根の要素をリストで返す
        """

        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        """
        グループの数
        """
        return len(self.roots())

    def all_group_members(self):
        """
        {ルート要素：[そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        """
        print()での表示用
        ルート要素:[そのグループに含まれる要素のリスト]を文字列で返す
        """

        return '\n'.join(f'{r}:{m}' for r, m in self.all_group_members().items())

n = I()
a = LI()
if n == 1:
    print(0)
    exit()
temp = 2*10**5
union = UnionFind(temp)
han = int(n/2)

for i in range(han):
    if a[i] != a[n-1-i]:
        union.union(a[i],a[n-1-i])

ans = 0
for i in range(temp+1):
    if union.par[i] < 0:
        ans += -union.par[i] - 1
print(ans)