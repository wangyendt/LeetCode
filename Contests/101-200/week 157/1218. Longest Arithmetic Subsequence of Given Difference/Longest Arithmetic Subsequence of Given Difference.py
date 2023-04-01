#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Longest Arithmetic Subsequence of Given Difference
@time: 2019/10/8 11:02
"""


class Solution:
    def longestSubsequence(self, arr: list, difference: int) -> int:
        res = {}
        for num in arr:
            res[num] = res[num - difference] + 1 if (num - difference) in res else 1
        return max(res.values())


so = Solution()
print(so.longestSubsequence(arr=[1, 3, 5, 7], difference=1))
print(so.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))
print(so.longestSubsequence(arr=[1, 2, 3, 4], difference=1))
print(so.longestSubsequence([7, -2, 8, 10, 6, 18, 9, -8, -5, 18, 13, -6, -17, -1, -6, -9, 9, 9], 1))
