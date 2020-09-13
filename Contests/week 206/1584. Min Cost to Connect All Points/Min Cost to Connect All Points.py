#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Min Cost to Connect All Points
@time: 2020/09/13 11:24
"""


class Solution:
    def minCostConnectPoints(self, points: list(list())) -> int:
        n = len(points)
        if len(points) == 1: return 0
        res = 0
        curr = 0  # select a random point as the starting point
        dis = [float('inf')] * n
        explored = set()

        for i in range(n - 1):
            x0, y0 = points[curr]
            explored.add(curr)
            for j, (x, y) in enumerate(points):
                if j in explored: continue
                dis[j] = min(dis[j], abs(x - x0) + abs(y - y0))

            delta, curr = min((d, j) for j, d in enumerate(dis))
            dis[curr] = float('inf')
            res += delta

        return int(res)
