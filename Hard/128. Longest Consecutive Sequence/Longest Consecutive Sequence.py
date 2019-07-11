#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Longest Consecutive Sequence.py 
@time: 2019/07/02
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def longestConsecutive(self, nums: list) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        dp = [1] * (n + 1)
        for i in range(1, n):
            if nums[i] - nums[i - 1] == 1:
                dp[i] = dp[i - 1] + 1
        return max(dp)
