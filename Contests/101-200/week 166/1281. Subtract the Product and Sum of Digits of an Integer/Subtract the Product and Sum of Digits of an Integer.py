#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Subtract the Product and Sum of Digits of an Integer
@time: 2019/12/9 15:31
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1
        while n:
            r = n % 10
            n = n // 10
            s += r
            p *= r
        return p - s


so = Solution()
print(so.subtractProductAndSum(234))
print(so.subtractProductAndSum(4421))
