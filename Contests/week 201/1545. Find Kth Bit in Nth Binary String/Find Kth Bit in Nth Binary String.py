#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find Kth Bit in Nth Binary String
@time: 2020/08/09 18:26
"""


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def flip(s):
            for t in s:
                if t == '0':
                    yield '1'
                else:
                    yield '0'

        cur = '0'
        for i in range(1, n):
            cur = cur + '1' + ''.join(list(flip(cur)))[::-1]
        return cur[k - 1]


so = Solution()
print(so.findKthBit(3, 1))
print(so.findKthBit(4, 11))
print(so.findKthBit(1, 1))
print(so.findKthBit(2, 3))
print(so.findKthBit(20, 1000000))
