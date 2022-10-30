#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find N Unique Integers Sum up to Zero
@time: 2020/1/3 15:02
"""


class Solution:
    def sumZero(self, n: int) -> list:
        ret = []
        if n % 2 == 0:
            for i in range(n // 2):
                ret.append(i + 1)
                ret.append(-i - 1)
        else:
            ret.append(0)
            for i in range(n // 2):
                ret.append(i + 1)
                ret.append(-i - 1)
        return ret


so = Solution()
print(so.sumZero(5))
print(so.sumZero(3))
print(so.sumZero(1))
