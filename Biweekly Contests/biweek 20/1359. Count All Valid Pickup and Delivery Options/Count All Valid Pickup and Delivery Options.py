#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count All Valid Pickup and Delivery Options
@time: 2020/2/26 17:02
"""

import math


class Solution:
    def countOrders(self, n: int) -> int:
        return (math.factorial(2 * n) >> n) % (10 ** 9 + 7)


so = Solution()
print(so.countOrders(1))
print(so.countOrders(2))
print(so.countOrders(3))
