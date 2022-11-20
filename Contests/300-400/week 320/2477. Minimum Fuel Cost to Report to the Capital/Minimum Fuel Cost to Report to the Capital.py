#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Fuel Cost to Report to the Capital.py 
@time: 2022/11/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import functools


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        res = collections.defaultdict(set)
        for r1, r2 in roads:
            res[r1].add(r2)
            res[r2].add(r1)
        # print(f'{roads=}')
        # print(f'{res=}')

        routine = collections.defaultdict(int)
        stack = [0]
        seen = {0}
        while stack:
            s = stack.pop()
            for t in res[s]:
                if t not in seen:
                    routine[t] = s
                    stack.append(t)
                    seen.add(t)
        # print(f'{routine=}')

        cnt = collections.defaultdict(int)
        seen = {0}

        @functools.lru_cache(None)
        def helper(cur: int):
            ans = 0
            for nei in res[cur]:
                if nei not in seen:
                    seen.add(nei)
                    ans += helper(nei)
            if cur != 0:
                cnt[cur] = ans + 1
            return ans + 1

        helper(0)
        # print(f'{cnt=}')

        ret = 0
        for i in range(len(roads) + 1):
            if i:
                ret += (cnt[i] - 1) // seats + 1
        return ret


so = Solution()
print(so.minimumFuelCost(roads=[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], seats=2), 7)
print(so.minimumFuelCost([[0, 1], [0, 2], [1, 3], [1, 4]], 5), 4)
print(so.minimumFuelCost([[0, 1], [1, 2]], 3), 2)
print(so.minimumFuelCost([[1, 0], [0, 2], [3, 1], [1, 4], [5, 0]], 1), 7)
print(so.minimumFuelCost([[1, 0], [1, 2], [3, 1], [4, 2]], 2), 5)
