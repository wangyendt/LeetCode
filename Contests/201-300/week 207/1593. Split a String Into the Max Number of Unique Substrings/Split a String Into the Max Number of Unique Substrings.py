#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Split a String Into the Max Number of Unique Substrings
@time: 2020/09/20 17:28
"""


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start: int, seen: set):
            if start == len(s): return 0
            res = 0
            for i in range(start + 1, len(s) + 1):
                part = s[start:i]
                if part not in seen:
                    seen.add(part)
                    res = max(res, backtrack(i, seen) + 1)
                    seen.discard(part)
            return res

        return backtrack(0, set())
