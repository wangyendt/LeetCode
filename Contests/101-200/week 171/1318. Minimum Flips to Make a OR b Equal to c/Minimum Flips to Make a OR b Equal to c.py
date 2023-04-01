#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Flips to Make a OR b Equal to c
@time: 2020/1/15 16:10
"""


class Solution:
    def minFlips(self, A: int, B: int, C: int) -> int:
        def f(a, b, c):
            if c == 0:
                if a == 1 and b == 0 or a == 0 and b == 1:
                    return 1
                elif a == 1 and b == 1:
                    return 2
                else:
                    return 0
            elif c == 1:
                if a == b == 0:
                    return 1
                else:
                    return 0

        ret = 0
        print(bin(A),bin(B),bin(C))
        while A or B or C:
            a_, b_, c_ = A & 1, B & 1, C & 1
            ret += f(a_, b_, c_)
            A >>= 1
            B >>= 1
            C >>= 1
        return ret


so = Solution()
print(so.minFlips(2, 6, 5))
print(so.minFlips(4, 2, 7))
print(so.minFlips(1, 2, 3))
print(so.minFlips(10000000, 2000000, 3000000))
