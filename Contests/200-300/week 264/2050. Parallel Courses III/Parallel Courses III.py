#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Parallel Courses III.py 
@time: 2021/10/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import functools


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = dict()
        for i in range(1, n + 2):
            g[i] = collections.defaultdict(list)
        for r1, r2 in relations:
            g[r1]['post'].append(r2)
            g[r2]['prev'].append(r1)

        for i in range(1, n + 1):
            if not g[i]['post']:
                g[i]['post'].append(n + 1)
                g[n + 1]['prev'].append(i)

        @functools.lru_cache(None)
        def dp(node):
            prevs = g[node]['prev']
            if not prevs and node != n + 1:
                return time[node - 1]
            else:
                res = 0
                for prev in prevs:
                    res = max(res, dp(prev))
                res += (time[node - 1] if node != n + 1 else 0)
                return res

        return dp(n + 1)


so = Solution()
print(so.minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]))
