#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Segment Sum After Removals.py 
@time: 2022/10/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.sum = {}
        self.maxSumSegment = 0

    def addAndMergeAdjSegment(self, u, value):
        self.parent[u] = u
        self.sum[u] = value
        self.maxSumSegment = max(self.maxSumSegment, value)
        if u - 1 in self.parent:
            self.union(u, u - 1)
        if u + 1 in self.parent:
            self.union(u, u + 1)

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return
        self.sum[pu] += self.sum[pv]
        self.parent[pv] = pu
        self.maxSumSegment = max(self.maxSumSegment, self.sum[pu])


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = UnionFind()

        ans = [0] * n
        for i in range(n - 1, -1, -1):
            ans[i] = uf.maxSumSegment
            q = removeQueries[i]
            uf.addAndMergeAdjSegment(q, nums[q])
        return ans
