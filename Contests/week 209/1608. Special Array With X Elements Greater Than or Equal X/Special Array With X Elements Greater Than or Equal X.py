#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Special Array With X Elements Greater Than or Equal X
@time: 2020/10/05 08:49
"""

from typing import *


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        ret = -1
        nums.sort()
        for i in range(len(nums)):
            if len(nums) - i <= nums[i] and (i == 0 or len(nums) - i > nums[i - 1]):
                ret = len(nums) - i
                break
        return ret
