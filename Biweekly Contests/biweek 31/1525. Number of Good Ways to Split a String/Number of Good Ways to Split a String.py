#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Good Ways to Split a String
@time: 2020/07/26 01:13
"""

import collections


class Solution:
    def numSplits(self, s: str) -> int:
        c1, c2 = collections.Counter(), collections.Counter(s)
        ret = 0
        for t in s:
            c1 += collections.Counter(t)
            c2 -= collections.Counter(t)
            l1, l2 = len(c1.items()), len(c2.items())
            if l1 == l2: ret += 1
            if l1 > l2: break
        return ret


so = Solution()
print(so.numSplits('aacaba'))
