#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Allocate Mailboxes
@time: 2020/06/13 23:33
"""

import functools
import sys


class Solution:
    def minDistance(self, houses: list, k: int) -> int:
        def dist(start: int, end: int):
            total = 0
            while start < end:
                total += houses[end] - houses[start]
                start += 1
                end -= 1
            return total

        @functools.lru_cache(None)
        def dfs(i: int, last: int, group: int) -> int:
            if i == n: return sys.maxsize
            if group == k - 1: return dist(i, n - 1)
            new_group = dfs(i + 1, i + 1, group + 1) + dist(last, i)
            no_new_group = dfs(i + 1, last, group)
            return min(new_group, no_new_group)

        n = len(houses)
        houses.sort()
        return dfs(0, 0, 0)
