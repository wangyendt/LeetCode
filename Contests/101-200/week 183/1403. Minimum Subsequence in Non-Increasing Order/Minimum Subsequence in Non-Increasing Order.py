#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Subsequence in Non-Increasing Order
@time: 2020/4/9 13:38
"""

import heapq


class Solution:
    def minSubsequence(self, nums: list) -> list:
        heapq._heapify_max(nums)
        total, s, res = sum(nums), 0, []
        while s <= total / 2:
            res.append(heapq._heappop_max(nums))
            s += res[-1]
        return res


so = Solution()
print(so.minSubsequence(nums=[4, 3, 10, 9, 8]))
print(so.minSubsequence(nums=[4, 4, 7, 6, 7]))
print(so.minSubsequence(nums=[6]))
