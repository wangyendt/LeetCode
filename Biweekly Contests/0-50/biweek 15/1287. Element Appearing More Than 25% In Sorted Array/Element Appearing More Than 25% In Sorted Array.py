#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Element Appearing More Than 25% In Sorted Array
@time: 2019/12/16 16:11
"""


class Solution:
    def findSpecialInteger(self, arr: list) -> int:
        p = 1
        last = arr[0]
        for i, a in enumerate(arr):
            if i > 0:
                if a == last:
                    p += 1
                    if 4 * p > len(arr):
                        return a
                else:
                    p = 1
                last = a
        return last


so = Solution()
print(so.findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]))
