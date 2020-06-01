#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count of Smaller Numbers After Self
@time: 2020/06/01 14:10
"""

import bisect


class Solution:
    def countSmaller(self, nums: list) -> list:
        res, ret = [], []
        for n in nums[::-1]:
            ret.append(bisect.bisect_left(res, n))
            bisect.insort(res, n)
        return ret[::-1]


so = Solution()
print(so.countSmaller([5, 2, 6, 1]))
print(so.countSmaller([5, 3, 3, 3, 2, 1]))
