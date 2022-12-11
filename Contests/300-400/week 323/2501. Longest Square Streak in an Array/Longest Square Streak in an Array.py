#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Longest Square Streak in an Array.py 
@time: 2022/12/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import math


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        idx = collections.defaultdict(int)
        dp = [0] * N
        for i, n in enumerate(nums):
            sqrt = int(math.sqrt(n))
            if sqrt * sqrt == n and sqrt in idx:
                dp[i] = dp[idx[sqrt]] + 1
            else:
                dp[i] = 1
            idx[n] = i
        ret = max(dp)
        if ret == 1:
            ret = -1
        return ret


so = Solution()
print(so.longestSquareStreak([4, 5, 4]))
