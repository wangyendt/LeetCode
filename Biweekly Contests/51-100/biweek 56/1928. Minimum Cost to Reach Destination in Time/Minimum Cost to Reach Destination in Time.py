# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Minimum Cost to Reach Destination in Time.py
@time: 2021/07/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *
import heapq


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)

        g = [[] for i in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))

        times = {}

        pq = [(passingFees[0], 0, 0)]

        while pq:
            cost, node, time = heapq.heappop(pq)

            if time > maxTime:
                continue

            if node == n - 1:
                return cost

            if node not in times or times[node] > time:
                times[node] = time
                for nbor, trip in g[node]:
                    heapq.heappush(pq, (passingFees[nbor] + cost, nbor, time + trip))

        return -1
