#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: String Compression II
@time: 2020/07/27 01:47
"""

import functools


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def counter(s, start, last, count, left):  # count increase from start
            if left < 0:
                return float('inf')
            if start >= len(s):
                return 0
            if s[start] == last:
                incr = 1 if count == 1 or count == 9 or count == 99 else 0
                return incr + counter(s, start + 1, last, count + 1, left)  # we keep it
            else:
                # keep it or delete it
                return min(1 + counter(s, start + 1, s[start], 1, left), counter(s, start + 1, last, count, left - 1))

        return counter(s, 0, "", 0, k)
