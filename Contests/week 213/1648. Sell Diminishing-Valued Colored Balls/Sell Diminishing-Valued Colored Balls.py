#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Sell Diminishing-Valued Colored Balls
@time: 2020/11/08 10:51
"""

from typing import *
import collections


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory = [list(inv) for inv in sorted(collections.Counter(inventory).items(), reverse=True) + [(0, 1)]]
        # print(inventory)
        ret = 0
        for i, (k, c) in enumerate(inventory):
            if i < len(inventory) - 1:
                # start, end = k, inventory[i + 1][0] + 1
                d, r = divmod(orders, c)
                start = k
                end = start - d + 1
                if end <= inventory[i + 1][0]:
                    ret += (start + inventory[i + 1][0] + 1) * (start - inventory[i + 1][0]) // 2 * c
                    # print(i, inventory[i + 1])
                    inventory[i + 1][1] += c
                    orders -= (start - inventory[i + 1][0]) * c
                else:
                    ret += (start + end) * (start - end + 1) // 2 * c
                    orders -= (start - end + 1) * c
                    ret += (end - 1) * orders
                    break
                # print(inventory, orders, ret)
        return ret % (10 ** 9 + 7)


so = Solution()
# print(so.maxProfit(inventory=[2, 5], orders=4))
# print(so.maxProfit(inventory=[3, 5], orders=6))
print(so.maxProfit(inventory=[2, 8, 4, 10, 6], orders=20))
# print(so.maxProfit(inventory=[1000000000], orders=1000000000))
