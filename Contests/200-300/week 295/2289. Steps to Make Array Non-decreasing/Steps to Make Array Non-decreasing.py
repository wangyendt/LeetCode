#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Steps to Make Array Non-decreasing.py 
@time: 2022/05/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        stack = []
        ret = 0
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
                ret = max(ret, dp[i])
            stack.append(i)
        return ret


so = Solution()
# print(so.totalSteps(nums=[5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]))
print(so.totalSteps([7, 14, 4, 14, 13, 2, 6, 13]))
