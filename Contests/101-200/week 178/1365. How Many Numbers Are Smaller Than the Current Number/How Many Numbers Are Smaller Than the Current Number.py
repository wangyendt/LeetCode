#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: How Many Numbers Are Smaller Than the Current Number
@time: 2020/3/5 13:52
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        return [sorted(nums).index(x) for x in nums]


so = Solution()
print(so.smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]))
print(so.smallerNumbersThanCurrent(nums=[6, 5, 4, 8]))
print(so.smallerNumbersThanCurrent(nums=[7, 7, 7, 7]))
