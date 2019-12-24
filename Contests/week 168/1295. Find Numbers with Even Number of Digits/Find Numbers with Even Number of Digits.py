#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find Numbers with Even Number of Digits
@time: 2019/12/24 10:41
"""


class Solution:
    def findNumbers(self, nums: list) -> int:
        ret = 0
        for n in nums:
            if len(str(n)) % 2 == 0: ret += 1
        return ret


so = Solution()
print(so.findNumbers(nums=[12, 345, 2, 6, 7896]))
print(so.findNumbers(nums=[555, 901, 482, 1771]))
