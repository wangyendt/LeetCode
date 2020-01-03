#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Replace Elements with Greatest Element on Right Side
@time: 2020/1/3 13:56
"""


class Solution:
    def replaceElements(self, arr: list) -> list:
        r_max = -1
        n = len(arr)
        for i in range(n):
            tmp = arr[-1 - i]
            arr[-1 - i] = r_max
            r_max = max(tmp, r_max)
        return arr


so = Solution()
print(so.replaceElements(arr=[17, 18, 5, 4, 6, 1]))
