#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Absolute Sum of Any Subarray
@time: 2021/02/06 22:33
"""

from typing import *
import sys


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def max_subarray(A):
            max_ending_here = max_so_far = A[0]
            for x in A[1:]:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far

        r1 = max_subarray(nums)
        r2 = max_subarray([-n for n in nums])
        return max(r1, r2)
