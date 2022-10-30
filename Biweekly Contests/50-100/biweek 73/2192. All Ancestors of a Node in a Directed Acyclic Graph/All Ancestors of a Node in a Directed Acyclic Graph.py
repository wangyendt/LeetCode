#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: All Ancestors of a Node in a Directed Acyclic Graph.py 
@time: 2022/03/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import functools


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        prev = collections.defaultdict(list)
        post = collections.defaultdict(list)
        for e1, e2 in edges:
            prev[e2].append(e1)
            post[e1].append(e2)

        # print(prev)
        # print(post)

        @functools.lru_cache(10000)
        def dp(i):
            if not prev[i]:
                return []
            res = set()
            for e in prev[i]:
                # print(dp(e))
                res.add(e)
                for e2 in dp(e):
                    res.add(e2)
                # print(i, e, res, prev[e])
            return list(sorted(res))

        ret = []
        for i in range(n):
            ret.append(list(sorted(set(dp(i)))))
        return ret


so = Solution()
print(so.getAncestors(n=8, edges=[[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]))
