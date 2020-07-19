#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Water Bottles
@time: 2020/07/20 00:12
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ret = numBottles
        while numBottles >= numExchange:
            d, r = divmod(numBottles, numExchange)
            ret += d
            numBottles = d + r
        return ret


so = Solution()
print(so.numWaterBottles(9, 3))
print(so.numWaterBottles(15, 4))
print(so.numWaterBottles(5, 5))
print(so.numWaterBottles(2, 3))
