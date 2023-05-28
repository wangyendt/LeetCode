"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Greatest Common Divisor Traversal.py
@time: 20230528
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        self.size = [1] * n

    def getFa(self, i):
        if i == self.fa[i]:
            return i
        self.fa[i] = self.getFa(self.fa[i])
        return self.fa[i]

    def merge(self, i, j):
        fi, fj = self.getFa(i), self.getFa(j)
        if fi == fj: return
        if self.size[fi] > self.size[fj]: fi, fj = fj, fi
        self.size[fj] += self.size[fi]
        self.fa[fi] = fj


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        fst = [-1] * (1 + max(nums))
        u = UnionFind(len(nums))
        for i, x in enumerate(nums):
            for p in range(2, x):
                if p * p > x: break
                if x % p != 0: continue
                if fst[p] != -1:
                    u.merge(fst[p], i)
                else:
                    fst[p] = i
                while x % p == 0: x //= p
            if x > 1:
                if fst[x] != -1:
                    u.merge(fst[x], i)
                else:
                    fst[x] = i
        return u.size[u.getFa(0)] == len(nums)
