#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Difference Between Largest and Smallest Value in Three Moves
@time: 2020/07/11 22:44
"""


class Solution:
    def minDifference(self, nums: list) -> int:
        if len(nums) <= 4: return 0
        nums.sort()
        return min(
            nums[-1] - nums[3], nums[-4] - nums[0],
            nums[-2] - nums[2], nums[-3] - nums[1]
        )
