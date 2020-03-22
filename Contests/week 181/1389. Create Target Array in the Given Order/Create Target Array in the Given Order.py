#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/23 0:54
@Author:  wang121ye
@File: Create Target Array in the Given Order.py
@Software: PyCharm
"""


class Solution:
    def createTargetArray(self, nums: list, index: list) -> list:
        ret = []
        for n, i in zip(nums, index):
            ret.insert(i, n)
        return ret


so = Solution()
print(so.createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))
print(so.createTargetArray(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]))
print(so.createTargetArray(nums=[1], index=[0]))
