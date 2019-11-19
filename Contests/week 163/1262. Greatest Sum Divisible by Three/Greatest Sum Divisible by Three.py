#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Greatest Sum Divisible by Three
@time: 2019/11/19 18:17
"""


class Solution:
    def maxSumDivThree(self, nums: list) -> int:
        mod0 = [n for n in nums if n % 3 == 0 and n > 0]
        mod1p = [n for n in nums if n % 3 == 1 and n > 0]
        mod1n = sorted([n for n in nums if n % 3 == 1 and n < 0])[-2:]
        mod2p = [n for n in nums if n % 3 == 2 and n > 0]
        mod2n = sorted([n for n in nums if n % 3 == 2 and n < 0])[-2:]
        ret = sum(mod0)
        ret += mod1p + mod2p
        if ret % 3 == 0:
            pass
        elif ret % 3 == 1:
            tmp = sum(mod2n)
            if tmp % 3 == 1:
                ret -=


