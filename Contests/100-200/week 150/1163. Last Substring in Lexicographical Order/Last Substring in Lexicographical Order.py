#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Last Substring in Lexicographical Order
@time: 2019/8/20 15:56
"""


class Solution:
    def lastSubstring(self, s: str) -> str:
        index = {c: i for i, c in enumerate(sorted(set(s)))}
        radix, val, cur, lo = len(index), 0, 0, 0
        for i in range(len(s) - 1, -1, -1):
            cur = index[s[i]] + cur / radix
            if cur >= val:
                lo, val = i, cur
        return s[lo:]
