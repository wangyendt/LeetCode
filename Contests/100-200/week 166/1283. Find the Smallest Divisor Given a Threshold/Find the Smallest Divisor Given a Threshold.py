#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find the Smallest Divisor Given a Threshold
@time: 2019/12/9 15:46
"""


class Solution:
    def smallestDivisor(self, nums, threshold):
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            if sum((i + m - 1) // m for i in nums) > threshold:
                l = m + 1
            else:
                r = m
        return l


so = Solution()
print(so.smallestDivisor([1, 2, 3], 1000000))
print(so.smallestDivisor(nums=[1, 2, 5, 9], threshold=6))
print(so.smallestDivisor(nums=[2, 3, 5, 7, 11], threshold=11))
print(so.smallestDivisor(nums=[19], threshold=5))
