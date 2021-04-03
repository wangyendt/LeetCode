#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: 3
@time: 2021/04/03 22:28
"""

from typing import *
import collections


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            if x == 0:
                return 0
            return int(str(x)[::-1].lstrip('0'))

        res = []
        for n in nums:
            res.append(n - rev(n))
        res = collections.Counter(res)
        ret = 0
        # print(res)
        for k, v in res.items():
            if v > 1:
                ret += v * (v - 1) // 2
        return ret % (10 ** 9 + 7)


so = Solution()
print(so.countNicePairs(nums=[42, 11, 1, 97]))
print(so.countNicePairs(nums=[42, 11, 1, 120, 0]))
