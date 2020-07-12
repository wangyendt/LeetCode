#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Best Position for a Service Centre
@time: 2020/07/12 11:49
"""

from scipy.optimize import minimize


class Solution:
    def getMinDistSum(self, positions: list(list())) -> float:
        x0 = sum([x for x, y in positions]) / len(positions)
        y0 = sum([y for x, y in positions]) / len(positions)

        def getCost(pt):
            avgX, avgY = pt
            cost = 0
            for x, y in positions:
                cost += ((x - avgX) ** 2 + (y - avgY) ** 2) ** 0.5
            return cost

        res = minimize(getCost, [x0, y0])
        return res.fun
