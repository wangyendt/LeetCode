#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Longest Happy String
@time: 2020/4/9 14:56
"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def helper(sa: str, sb: str, sc: str, a: int, b: int, c: int) -> str:
            if a < b: return helper(sb, sa, sc, b, a, c)
            if b < c: return helper(sa, sc, sb, a, c, b)
            if b == 0: return sa * min(2, a)
            use_a = min(2, a)
            use_b = 1 if a - use_a >= b else 0
            return sa * use_a + sb * use_b + helper(sa, sb, sc, a - use_a, b - use_b, c)

        return helper('a', 'b', 'c', a, b, c)


so = Solution()
print(so.longestDiverseString(1, 1, 7))
print(so.longestDiverseString(2, 2, 1))
print(so.longestDiverseString(7, 1, 0))
