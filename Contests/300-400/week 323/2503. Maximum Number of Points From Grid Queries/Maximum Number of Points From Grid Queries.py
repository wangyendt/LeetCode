#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Number of Points From Grid Queries.py 
@time: 2022/12/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        sq = sorted(queries)
        h = {}
        vs = set()
        vs.add((0, 0))
        pq = [(grid[0][0], 0, 0)]
        for i in sq:
            while pq:
                v, a, b = pq[0]
                if v >= i: break
                heapq.heappop(pq)
                for c, d in (a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1):
                    if c < 0 or c >= m or d < 0 or d >= n: continue
                    if (c, d) in vs: continue
                    heapq.heappush(pq, (grid[c][d], c, d))
                    vs.add((c, d))
            h[i] = len(vs) - len(pq)

        return [h[i] for i in queries]
