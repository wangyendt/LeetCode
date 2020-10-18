#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Graph Connectivity With Threshold
@time: 2020/10/19 00:26
"""

from typing import *


# Feel free to copy this class for later reuse!
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return False
        if self.size[pu] > self.size[pv]:  # Union by larger size
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True


class Solution(object):
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n + 1)
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):  # step by i
                if i > threshold:
                    uf.union(i, j)
        ans = []
        for q in queries:
            pa = uf.find(q[0])
            pb = uf.find(q[1])
            ans.append(pa == pb)
        return ans
