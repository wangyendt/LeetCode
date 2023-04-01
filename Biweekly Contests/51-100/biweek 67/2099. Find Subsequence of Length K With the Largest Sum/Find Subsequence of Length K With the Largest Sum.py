#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Subsequence of Length K With the Largest Sum.py 
@time: 2021/12/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sorted_idx = sorted(range(len(nums)), key=lambda x: nums[x])
        res = {s: i for i, s in enumerate(sorted_idx)}
        ret = []
        for i, n in enumerate(nums):
            if res[i] + k >= len(nums):
                ret.append(n)
        return ret


so = Solution()
# print(so.maxSubsequence(nums=[2, 1, 3, 3], k=2))
print(so.maxSubsequence([63, -74, 61, -17, -55, -59, -10, 2, -60, -65], 9))
