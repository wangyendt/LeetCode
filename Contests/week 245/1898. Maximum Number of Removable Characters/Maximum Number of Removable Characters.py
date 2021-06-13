#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Number of Removable Characters
@time: 2021/06/13 22:48
"""

from typing import *


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def check(m):
            i = j = 0
            remove = set(removable[:m + 1])
            while i < len(s) and j < len(p):
                if i in remove:
                    i += 1
                    continue
                if s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1

            return j == len(p)

        # search interval is [lo, hi)
        lo, hi = 0, len(removable) + 1

        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid

        return lo if lo < len(removable) else lo - 1
