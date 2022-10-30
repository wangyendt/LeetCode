#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Longest Subarray of 1's After Deleting One Element
@time: 2020/06/27 22:39
"""

import functools
import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    def longestSubarray(self, nums: list) -> int:
        num_of_one = sum([1 for n in nums if n == 1])
        if num_of_one >= len(nums) - 1: return len(nums) - 1

        @functools.lru_cache(None)
        def helper(ind, status, cnt1=0):
            ret[0] = max(ret[0], cnt1)
            if ind == len(nums):
                return
            n = nums[ind]
            if status == 0:
                if n == 0:
                    helper(ind + 1, 0)
                elif n == 1:
                    helper(ind + 1, 1, 1)
            elif status == 1:
                if n == 1:
                    helper(ind + 1, 1, cnt1 + 1)
                elif n == 0:
                    helper(ind + 1, 2, cnt1)
                    helper(ind + 1, 0)
            elif status == 2:
                if n == 1:
                    helper(ind + 1, 2, cnt1 + 1)
                elif n == 0:
                    helper(ind + 1, 0)

        ret = [0]
        helper(0, 0)
        return ret[0]


so = Solution()
print(so.longestSubarray(nums=[1, 1, 0, 1]))
print(so.longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(so.longestSubarray(nums=[1, 1, 1]))
print(so.longestSubarray(nums=[1, 1, 0, 0, 1, 1, 1, 0, 1]))
print(so.longestSubarray(nums=[0, 0, 0]))
# print(so.longestSubarray(nums=[1] * 100000))
# print(so.longestSubarray(nums=[1, 0, 1, 0, 0, 1] + [1] * 100000))
# print(so.longestSubarray(nums=[1] * 100000 + [1, 0, 1, 0, 0, 1]))
print(so.longestSubarray([1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
