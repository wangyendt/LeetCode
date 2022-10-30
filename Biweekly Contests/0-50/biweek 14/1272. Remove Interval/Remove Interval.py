#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Remove Interval
@time: 2019/12/2 13:58
"""


class Solution:
    def removeInterval(self, intervals: list(list()), toBeRemoved: list) -> list(list()):
        a, b = toBeRemoved
        ret = []
        for ia, ib in intervals:
            if ia < ib <= a:
                ret.append([ia, ib])
            elif ia < a < ib <= b:
                ret.append([ia, a])
            elif ia < a and ib > b:
                ret.append([ia, a])
                ret.append([b, ib])
            elif a <= ia < ib <= b:
                pass
            elif a <= ia <= b < ib:
                ret.append([b, ib])
            elif ia >= b:
                ret.append([ia, ib])
        return ret


so = Solution()
print(so.removeInterval(intervals=[[0, 2], [3, 4], [5, 7]], toBeRemoved=[1, 6]))
print(so.removeInterval(intervals=[[0, 5]], toBeRemoved=[2, 3]))
print(so.removeInterval([[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], [-1, 4]))
print(so.removeInterval([[0, 100]], [0, 50]))
