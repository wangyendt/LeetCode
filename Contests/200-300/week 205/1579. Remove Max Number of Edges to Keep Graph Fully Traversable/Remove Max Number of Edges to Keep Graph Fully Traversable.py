#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Remove Max Number of Edges to Keep Graph Fully Traversable.py 
@time: 2020/09/06
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class UnionFindSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n
        self.size = 1

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        elif self.ranks[pv] > self.ranks[pu]:
            self.parents[pu] = pv
        else:
            self.parents[pu] = pv
            self.ranks[pv] += 1
        self.size += 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list(list())) -> int:
        uf1, uf2 = UnionFindSet(n), UnionFindSet(n)
        ans = 0
        for t, u, v in edges:
            if t != 3:
                continue
            if not uf1.union(u - 1, v - 1) or not uf2.union(u - 1, v - 1):
                ans += 1

        for t, u, v in edges:
            if t == 1 and not uf1.union(u - 1, v - 1):
                ans += 1
            elif t == 2 and not uf2.union(u - 1, v - 1):
                ans += 1

        if uf1.size != n or uf2.size != n: return -1
        return ans
