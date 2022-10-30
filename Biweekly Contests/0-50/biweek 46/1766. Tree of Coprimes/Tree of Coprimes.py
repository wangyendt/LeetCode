#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Tree of Coprimes.py 
@time: 2021/02/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        tree = {}  # tree as adjacency list
        for u, v in edges:
            tree.setdefault(u, []).append(v)
            tree.setdefault(v, []).append(u)

        ans = [-1] * len(nums)
        path = {}  # val -> list of position & depth
        seen = {0}

        def gcd(a, b):
            if a < b: a, b = b, a
            if b == 1: return 1
            if b == 0: return a
            return gcd(a % b, b)

        def fn(k, i):
            """Populate ans via dfs."""
            ii = -1
            for x in path:
                if gcd(nums[k], x) == 1:  # coprime
                    if path[x] and path[x][-1][1] > ii:
                        ans[k] = path[x][-1][0]
                        ii = path[x][-1][1]

            path.setdefault(nums[k], []).append((k, i))
            for kk in tree.get(k, []):
                if kk not in seen:
                    seen.add(kk)
                    fn(kk, i + 1)
            path[nums[k]].pop()

        fn(0, 0)
        return ans
