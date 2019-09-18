#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: K-Concatenation Maximum Sum
@time: 2019/9/17 15:14
"""

import sys


class Solution:
    def kConcatenationMaxSum(self, arr: list, k: int) -> int:
        def find_max_sub_array_sum(arr):
            dp = [-sys.maxsize] * (len(arr) + 1)
            for ai, a in enumerate(arr):
                dp[ai + 1] = max(dp[ai] + a, a)
            return max(dp)

        if k == 1: return find_max_sub_array_sum(arr)
        if k == 2: return find_max_sub_array_sum(arr * 2)
        max1, max2 = -sys.maxsize, -sys.maxsize
        agg_sum1, agg_sum2 = 0, 0
        for a in arr:
            agg_sum1 += a
            max1 = max(max1, agg_sum1)
        for a in arr[::-1]:
            agg_sum2 += a
            max2 = max(max2, agg_sum2)
        if sum(arr) >= 0:
            return max(max1 + max2 + (k - 2) * sum(arr),
                       find_max_sub_array_sum(arr),
                       find_max_sub_array_sum(arr * 2), 0) % 1000000007
        else:
            return max(find_max_sub_array_sum(arr),
                       find_max_sub_array_sum(arr * 2), 0) % 1000000007

    def kConcatenationMaxSum2(self, arr: list, k: int, mod=10 ** 9 + 7) -> int:
        def Kadane(arr, res=0, cur=0):
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            return res

        return ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2)) % mod if k > 1 else Kadane(arr) % mod


so = Solution()
print(so.kConcatenationMaxSum(arr=[1, 2], k=3))
print(so.kConcatenationMaxSum(arr=[1, -2, 1], k=5))
print(so.kConcatenationMaxSum(arr=[-1, -2], k=7))
