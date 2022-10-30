#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Sets of K Non-Overlapping Line Segments
@time: 2020/10/18 21:37
"""


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        res = 1
        for i in range(1, k * 2 + 1):
            res *= n + k - i
            res //= i
        return res % (10 ** 9 + 7)
