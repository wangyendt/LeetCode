#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Different Subsequences GCDs
@time: 2021/04/04 12:29
"""

from typing import *
import math


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        res = 0
        all_nums = set(nums)
        for i in range(1, 200001):
            current_gcd = None
            for k in range(i, 200001, i):
                if k in all_nums:
                    if current_gcd is None:
                        current_gcd = k
                    else:
                        current_gcd = math.gcd(current_gcd, k)
                    if current_gcd == i:
                        res += 1
                        break
        return res
