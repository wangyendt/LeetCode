#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Sort Integers by The Number of 1 Bits
@time: 2020/2/26 16:15
"""


class Solution:
    def sortByBits(self, arr: list) -> list:
        def calc_one_nums(num: int):
            ret = 0
            while num:
                num &= num - 1
                ret += 1
            return ret

        res = []
        for a in arr:
            res.append((a, calc_one_nums(a)))
        return [a[0] for a in sorted(res, key=lambda x: (x[1], x[0]))]


so = Solution()
print(so.sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(so.sortByBits(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
print(so.sortByBits(arr=[10000, 10000]))
print(so.sortByBits(arr=[2, 3, 5, 7, 11, 13, 17, 19]))
print(so.sortByBits(arr=[10, 100, 1000, 10000]))
