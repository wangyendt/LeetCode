#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Data Stream as Disjoint Intervals
@time: 2020/07/18 13:16
"""

import bisect


class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = [[float('-inf'), float('-inf')], [float('inf'), float('inf')]]

    def addNum(self, val: int) -> None:
        i = bisect.bisect(self.intervals, [val])
        ps, pe = self.intervals[i - 1]
        ns, ne = self.intervals[i]

        if pe == val - 1 and ns == val + 1:
            self.intervals = self.intervals[:i - 1] + [[ps, ne]] + self.intervals[i + 1:]
        elif pe == val - 1:
            self.intervals[i - 1][1] = val
        elif ns == val + 1:
            self.intervals[i][0] = val
        elif pe < val - 1 and ns > val + 1:
            self.intervals = self.intervals[:i] + [[val, val]] + self.intervals[i:]

    def getIntervals(self) -> list(list()):
        return self.intervals[1:-1]

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
