#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Max Value of Equation
@time: 2020/06/28 15:53
"""

import heapq
import sys


class Solution:
    def findMaxValueOfEquation(self, points: list(list()), k: int) -> int:
        h = []
        ret = -sys.maxsize
        for px, py in points:
            while h and px - h[0][1] > k:
                heapq.heappop(h)
            if h:
                ret = max(ret, px + py - h[0][0])
            heapq.heappush(h, (px - py, px))
        return ret
