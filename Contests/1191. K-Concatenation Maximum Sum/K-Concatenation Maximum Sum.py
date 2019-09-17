#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: K-Concatenation Maximum Sum
@time: 2019/9/17 15:14
"""


class Solution:
    def kConcatenationMaxSum(self, arr: list, k: int) -> int:
        def find_max_sub_array_sum(arr):
            dp = [0] * (len(arr)+1)
            for ai, a in enumerate(arr):
                dp[ai+1] = max(dp[ai]+a, a)
            return max(dp)
        print(find_max_sub_array_sum( ))
