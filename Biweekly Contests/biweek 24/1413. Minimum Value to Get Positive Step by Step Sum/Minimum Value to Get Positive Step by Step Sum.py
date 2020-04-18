#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/18 22:32
@Author:  wang121ye
@File: Minimum Value to Get Positive Step by Step Sum.py
@Software: PyCharm
"""


class Solution:
    def minStartValue(self, nums: list) -> int:
        acc_nums = []
        res = 0
        ret = 1
        for n in nums:
            res += n
            acc_nums.append(res)
            ret = max(ret, 1 - res)  # min(ret, 1-res)
        return ret


so = Solution()
print(so.minStartValue([-3, 2, -3, 4, 2]))
print(so.minStartValue([1, 2]))
print(so.minStartValue([1, -2, -3]))
