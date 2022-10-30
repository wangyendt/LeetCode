#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Paint House III
@time: 2020/06/07 10:55
"""

import functools


class Solution:
    def minCost(self, houses: list, cost: list(list()), m: int, n: int, target: int) -> int:
        # C is matrix , C[i][j] cost to paint ith house jth color
        INF = float('inf')

        @functools.lru_cache(None)
        def dp(i, j, k):
            # prev color was j
            # min cost, currently k neighborhoods
            if i == m:
                return 0 if k == target else INF
            ans = INF

            for new_color in (range(n) if houses[i] == 0 else [houses[i] - 1]):
                c = cost[i][new_color]
                bns = c + dp(i + 1, new_color, k + (new_color != j))
                if bns < ans: ans = bns
            return ans

        ans = dp(0, -1, 0)
        if ans == INF: return -1
        for i, x in enumerate(houses):
            if x:
                ans -= cost[i][x - 1]
        return ans
