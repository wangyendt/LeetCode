#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Cost to Split an Array.py 
@time: 2023/01/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [0] * N
        iv = 0
        cnter1 = collections.defaultdict(int)
        for i, n in enumerate(nums):
            cnter1[n] += 1
            if cnter1[n] == 1:
                iv += 1
            elif cnter1[n] == 2:
                iv -= 1
            if i == 0:
                dp[i] = k
            else:
                res = 1e10
                iv2 = 0
                cnter2 = collections.defaultdict(int)
                for j in range(i, -1, -1):
                    cnter2[nums[j]] += 1
                    if cnter2[nums[j]] == 1:
                        iv2 += 1
                    elif cnter2[nums[j]] == 2:
                        iv2 -= 1
                    res = min(res, (dp[j - 1] if j >= 1 else 1e11) + k + i - j + 1 - iv2)
                dp[i] = min(res, k + i + 1 - iv)
        return dp[-1]


so = Solution()
print(so.minCost(nums=[1, 2, 1, 2, 1, 3, 3], k=2))
