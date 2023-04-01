#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Convert Integer to the Sum of Two No-Zero Integers
@time: 2020/1/15 16:03
"""


class Solution:
    def getNoZeroIntegers(self, n: int) -> list:
        a = 1
        while True:
            b = n - a
            if '0' not in str(int(a)) and '0' not in str(int(b)):
                return [a, b]
            a = a + 1


so = Solution()
print(so.getNoZeroIntegers(2))
print(so.getNoZeroIntegers(11))
print(so.getNoZeroIntegers(69))
print(so.getNoZeroIntegers(1010))
