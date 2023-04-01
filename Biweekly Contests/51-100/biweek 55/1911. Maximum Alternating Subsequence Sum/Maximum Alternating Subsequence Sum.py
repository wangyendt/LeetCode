#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Alternating Subsequence Sum.py 
@time: 2021/06/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import sys


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        inf = sys.maxsize
        dp1 = [-1] * n
        dp2 = [inf] * n
        for i in range(n)[::-1]:
            if i == n - 1:
                dp1[i] = nums[i]
                dp2[i] = 0
            else:
                dp1[i] = max(dp1[i + 1], nums[i] - dp2[i + 1])
                dp2[i] = min(dp2[i + 1], nums[i] - dp1[i + 1])
        return dp1[0]


so = Solution()
print(so.maxAlternatingSum(nums=[6, 2, 1, 2, 4, 5]))
