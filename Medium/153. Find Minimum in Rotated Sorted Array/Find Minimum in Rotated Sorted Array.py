#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find Minimum in Rotated Sorted Array
@time: 2019/8/22 23:16
"""


class Solution:
    def findMin(self, nums: list) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[r] > nums[m]:
                r = m
            else:
                l = m + 1
        return nums[l]


so = Solution()
print(so.findMin([4, 5, 6, 7, 0, 1, 2]))
