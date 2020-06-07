#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count of Range Sum
@time: 2020/06/07 02:08
"""

import collections


class Solution:
    def countRangeSum(self, nums: list, lower: int, upper: int) -> int:
        # -2，5，-1, 4
        # -2，3，2, 6
        cumsum = [0]
        for n in nums:
            cumsum.append(n + cumsum[-1])
        res = collections.defaultdict(int)
        ret = 0
        for cum in cumsum:
            for tar in range(lower, upper + 1):
                if cum - tar in res:
                    ret += res[cum - tar]
            res[cum] += 1
        return ret


so = Solution()
print(so.countRangeSum(nums=[-2, 5, -1], lower=-2, upper=2))
