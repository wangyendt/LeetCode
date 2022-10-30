#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Sequential Digits
@time: 2019/12/16 17:35
"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> list:
        ret = []
        for i in range(1, 10):
            for j in range(i + 1, 10):
                res = int(''.join(map(str, range(i, j + 1))))
                if low <= res <= high:
                    ret.append(res)
        return sorted(ret)


so = Solution()
print(so.sequentialDigits(low=100, high=300))
print(so.sequentialDigits(low=1000, high=13000))
print(so.sequentialDigits(low=1000, high=130000000))
