#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Time Visiting All Points
@time: 2019/11/27 14:05
"""


class Solution:
    def minTimeToVisitAllPoints(self, points: list(list())) -> int:
        def min_time(start, end):
            return max(abs(start[0] - end[0]), abs(start[1] - end[1]))

        if len(points) == 1:
            ret = 0
        else:
            ret = 0
            for i in range(1, len(points)):
                ret += min_time(points[i - 1], points[i])
        return ret


so = Solution()
print(so.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
print(so.minTimeToVisitAllPoints([[3, 2], [-2, 2]]))
