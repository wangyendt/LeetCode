#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Final Prices With a Special Discount in a Shop
@time: 2020/06/13 22:34
"""


class Solution:
    def finalPrices(self, prices: list) -> list:
        ret = []
        for i, p in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if prices[j] <= p:
                    ret.append(p - prices[j])
                    break
            else:
                ret.append(p)
        return ret
