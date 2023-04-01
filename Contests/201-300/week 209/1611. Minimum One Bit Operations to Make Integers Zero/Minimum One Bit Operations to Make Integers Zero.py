#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum One Bit Operations to Make Integers Zero
@time: 2020/10/05 10:30
"""


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            n &= n - 1
        return abs(res)
