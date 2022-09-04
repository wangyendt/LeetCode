#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if There is a Valid Partition For The Array.py 
@time: 2022/09/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False for i in range(len(nums) + 1)]
        dp[0] = True
        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                dp[i + 1] |= dp[i - 1]
            if i - 2 >= 0 and nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                dp[i + 1] |= dp[i - 2]
            if i - 2 >= 0 and nums[i] - 1 == nums[i - 1] and nums[i - 1] - 1 == nums[i - 2]:
                dp[i + 1] |= dp[i - 2]
        return dp[-1]
