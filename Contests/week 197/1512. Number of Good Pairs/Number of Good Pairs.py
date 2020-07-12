#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: 1512. Number of Good Pairs
@time: 2020/07/12 10:32
"""

import collections


class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        cnter = collections.Counter(nums)
        ret = 0
        for k, v in cnter.items():
            if v > 1:
                ret += v * (v - 1) // 2
        return ret
