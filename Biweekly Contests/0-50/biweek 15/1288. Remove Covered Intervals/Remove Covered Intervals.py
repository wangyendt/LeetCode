#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Remove Covered Intervals
@time: 2019/12/16 16:16
"""


class Solution:
    def removeCoveredIntervals(self, intervals: list(list())) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        r = intervals[0][0] - 1
        ret = len(intervals)
        for x, y in intervals:
            if y <= r:
                ret -= 1
            else:
                r = y
        return ret


so = Solution()
print(so.removeCoveredIntervals(intervals=[[1, 4], [3, 6], [2, 8]]))
