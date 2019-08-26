#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find Peak Element
@time: 2019/8/23 1:27
"""


class Solution:
    def findPeakElement(self, nums: list) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1
        return l


so = Solution()
print(so.findPeakElement([1, 2, 3, 1]))
