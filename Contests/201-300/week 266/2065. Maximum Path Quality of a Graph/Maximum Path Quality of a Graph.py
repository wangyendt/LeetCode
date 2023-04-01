#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Path Quality of a Graph.py 
@time: 2021/11/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        G = collections.defaultdict(dict)
        for i, j, t in edges:
            G[i][j] = G[j][i] = t

        def dfs(i, seen, time):
            res = sum(values[j] for j in seen) if i == 0 else 0
            for j in G[i]:
                if time >= G[i][j]:
                    res = max(res, dfs(j, seen | {j}, time - G[i][j]))
            return res

        return dfs(0, {0}, maxTime)
