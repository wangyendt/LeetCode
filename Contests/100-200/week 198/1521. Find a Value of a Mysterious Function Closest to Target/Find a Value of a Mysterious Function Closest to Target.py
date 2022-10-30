#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find a Value of a Mysterious Function Closest to Target
@time: 2020/07/20 01:42
"""


class Solution:
    def closestToTarget(self, arr: list, target: int) -> int:
        s, ans = set(), float('inf')
        for a in arr:
            s = {a & b for b in s} | {a}
            for c in s:
                ans = min(ans, abs(c - target))
        return ans
