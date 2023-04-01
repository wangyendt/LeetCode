#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Swaps to Make Strings Equal
@time: 2019/11/8 11:32
"""

import collections


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if (collections.Counter(s1)['x'] + collections.Counter(s2)['x']) % 2 == 1:
            return -1
        ret = 0
        dx, dy = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    dx += 1
                else:
                    dy += 1
        d1, r1 = divmod(dx, 2)
        d2, r2 = divmod(dy, 2)
        ret += d1 + d2 + 2 * ((r1 + r2) // 2)
        return ret


so = Solution()
print(so.minimumSwap('xxy', 'xxx'))
print(so.minimumSwap(s1="xx", s2="yy"))
print(so.minimumSwap(s1="xy", s2="yx"))
print(so.minimumSwap(s1="xxyyxyxyxx", s2="xyyxyxxxyx"))
