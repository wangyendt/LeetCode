#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Product Subarray
@time: 2019/8/22 22:50
"""

import sys


class Solution:
    def maxProduct(self, nums: list) -> int:
        if not nums: raise ValueError()
        if len(nums) == 1: return nums[0]
        pos = neg = 0
        ans = -sys.maxsize - 1
        for n in nums:
            if n > 0:
                pos, neg = max(n, n * pos), min(0, n * neg)
            else:
                pos, neg = max(0, n * neg), min(n, n * pos)
            ans = max(pos, ans)
        return ans
