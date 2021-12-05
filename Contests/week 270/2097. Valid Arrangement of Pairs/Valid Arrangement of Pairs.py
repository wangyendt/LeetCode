#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Valid Arrangement of Pairs.py 
@time: 2021/12/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        degree = collections.defaultdict(int)  # net out degree
        for x, y in pairs:
            graph[x].append(y)
            degree[x] += 1
            degree[y] -= 1

        for k in degree:
            if degree[k] == 1:
                x = k
                break

        ans = []

        def fn(x):
            """Return Eulerian path via dfs."""
            while graph[x]: fn(graph[x].pop())
            ans.append(x)

        fn(x)
        ans.reverse()
        return [[ans[i], ans[i + 1]] for i in range(len(ans) - 1)]
