#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Total Space Wasted With K Resizing Operations.py 
@time: 2021/08/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import functools


class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)

        presum = [0]
        for nn in nums:
            presum.append(nn + presum[-1])

        def get_sum(i, j):
            return presum[j + 1] - presum[i]

        @functools.lru_cache(None)
        def dp(i, t):
            if i == n: return 0
            if t == 0:
                return max(nums[i:]) * (n - i) - get_sum(i, n - 1)
            ret = float('inf')
            mx = 0
            for j in range(i, n):
                mx = max(mx, nums[j])
                ret = min(ret, mx * (j - i + 1) - get_sum(i, j) + dp(j + 1, t - 1))
            return ret

        return dp(0, k)


so = Solution()
print(so.minSpaceWastedKResizing([10, 20], 0))
