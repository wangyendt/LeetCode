# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Maximum Profit of Operating a Centennial Wheel.py
@time: 2020/09/27
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ret, res = 1, -1
        board = 0
        wait = 0
        for i, cus in enumerate(customers):
            prep = cus + wait
            if prep > 4:
                cur = 4
                wait = prep - 4
            else:
                cur = prep
                wait = 0
            board += cur
            cost = board * boardingCost - (i + 1) * runningCost
            if cost > res:
                res = cost
                ret = i + 1
        n = len(customers)
        while wait > 0:
            n += 1
            cur = min(wait, 4)
            board += cur
            wait -= cur
            cost = board * boardingCost - n * runningCost
            if cost > res:
                res = cost
                ret = n
        return ret if res > 0 else -1


so = Solution()
# print(so.minOperationsMaxProfit(customers=[8, 3], boardingCost=5, runningCost=6))
print(so.minOperationsMaxProfit(customers=[10, 10, 6, 4, 7], boardingCost=3, runningCost=8))
