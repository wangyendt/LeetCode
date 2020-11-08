#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Create Sorted Array through Instructions
@time: 2020/11/08 11:25
"""

from typing import *
import bisect


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        ret = 0
        for ins in instructions:
            l = bisect.bisect_left(nums, ins)
            r = bisect.bisect_right(nums, ins)
            ret += min(l, len(nums) - r)
            nums[l:l] = [ins]
            # bisect.insort_left(nums, ins)
        # print(len(instructions))
        return ret % (10 ** 9 + 7)


so = Solution()
print(so.createSortedArray([1, 5, 6, 2]))
