#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Concatenation of Consecutive Binary Numbers
@time: 2020/12/06 10:40
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ret = 0
        l = 0
        # for i in range(n, 0, -1):
        #     ret += i << l
        #     l += i.bit_length()  # len(bin(i)) - 2
        #     print(i.bit_length())
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                l += 1
            ret = ((ret << l) | i) % (10 ** 9 + 7)
        return ret % (10 ** 9 + 7)


so = Solution()
print(so.concatenatedBinary(12))
print(so.concatenatedBinary(100000))
