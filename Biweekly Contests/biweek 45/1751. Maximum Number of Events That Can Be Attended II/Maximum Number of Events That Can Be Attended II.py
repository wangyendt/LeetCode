#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Number of Events That Can Be Attended II
@time: 2021/02/06 23:18
"""

from typing import *
import bisect


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)

        # dp[i][j]: maximum value you can get from i sorted by end time events using j operations.
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        events.sort(key=lambda x: (x[1], x[0]))  # Sort by end time
        endTimes = [e[1] for e in events]  # End times array. Used for binary search

        for i in range(1, n + 1):
            # idx is the leftmost idx that events[i - 1] does not intersect with events[idx - 1]
            idx = bisect.bisect_left(endTimes, events[i - 1][0])
            for j in range(1, k + 1):
                # Not taking the current events[i - 1]
                dp[i][j] = max(dp[i][j], dp[i - 1][j])

                # Since events[idx - 1] not intersect with events[i - 1]
                # You can take the current event
                dp[i][j] = max(dp[i][j], dp[idx][j - 1] + events[i - 1][2])
        return dp[n][k]


so = Solution()
# print(so.maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2))
# print(so.maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 10]], k=2))
# print(so.maxValue(events=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], k=3))
print(
    so.maxValue([[87, 95, 42], [3, 42, 37], [20, 42, 100], [53, 84, 80], [10, 88, 38], [25, 80, 57], [18, 38, 33]], 3))
