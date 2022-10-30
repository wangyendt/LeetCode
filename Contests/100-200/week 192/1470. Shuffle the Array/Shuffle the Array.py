#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Shuffle the Array
@time: 2020/06/07 10:30
"""


class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        return sum(map(list, zip(*[nums[:n], nums[n:]])), [])


so = Solution()
print(so.shuffle(nums=[2, 5, 1, 3, 4, 7], n=3))
print(so.shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4))
print(so.shuffle(nums=[1, 1, 2, 2], n=2))
