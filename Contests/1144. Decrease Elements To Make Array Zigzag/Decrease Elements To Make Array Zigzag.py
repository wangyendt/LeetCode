#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Decrease Elements To Make Array Zigzag
@time: 2019/8/13 19:24
"""

import sys


class Solution:
    def movesToMakeZigzag(self, nums: list) -> int:
        nums = [sys.maxsize] + nums + [sys.maxsize]
        odd, even = 0, 0
        for i in range(1, len(nums) - 1):
            if i % 2:
                odd += max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
            else:
                even += max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
        return min(odd, even)


so = Solution()
print(so.movesToMakeZigzag([9, 6, 1, 6, 2]), 4)
print(so.movesToMakeZigzag([1,2,3]), 2)
