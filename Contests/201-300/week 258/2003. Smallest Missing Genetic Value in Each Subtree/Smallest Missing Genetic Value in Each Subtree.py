#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Smallest Missing Genetic Value in Each Subtree.py 
@time: 2021/09/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        g = [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p != -1: g[p].append(i)

        res = [1] * n
        if 1 not in nums: return res  # 1 is missing for all nodes

        seen = [False] * (n + 1)  # record seen genetic values

        def scan(p, prev):  # dfs. put all values in this subtree into seen[]
            if nums[p] <= n: seen[nums[p]] = True
            for q in g[p]:
                if q != prev: scan(q, -1)  # prevent duplicated visits

        prev, p = -1, nums.index(1)
        cur = 0  # max genetic value seen so far
        while p != -1:
            scan(p, prev)
            while cur + 1 <= n and seen[cur + 1]: cur += 1
            res[p] = cur + 1
            prev, p = p, parents[p]

        return res


so = Solution()
print(so.smallestMissingValueSubtree(parents=[-1, 0, 0, 2], nums=[1, 2, 3, 4]))
