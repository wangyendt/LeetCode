#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: House Robber II.py 
@time: 2019/09/04
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def rob(self, nums: list) -> int:
        def helper(arr):
            if not arr: return 0
            if len(arr) == 1: return arr[0]
            if len(arr) == 2: return max(arr)

            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[:2])
            dp[2] = max(arr[0] + arr[2], arr[1])
            for i in range(3, len(dp)):
                dp[i] = max(dp[i - 2], dp[i - 3]) + arr[i]
            return max(dp[-2:])

        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))


so = Solution()
print(so.rob([2, 3, 2]))
print(so.rob([1, 2, 3, 1]))
print(so.rob([2, 7, 9, 3, 1]))
