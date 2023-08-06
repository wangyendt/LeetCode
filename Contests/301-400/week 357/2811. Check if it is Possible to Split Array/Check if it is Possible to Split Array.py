#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if it is Possible to Split Array.py 
@time: 2023/08/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import functools


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        prefix = [0]

        @functools.lru_cache(None)
        def helper(i, j):
            if j - i <= 1: return True
            return get_sum_i_j(i, j - 1) >= m and helper(i, j - 1) or get_sum_i_j(i + 1, j) >= m and helper(i + 1, j)

        for n in nums:
            prefix.append(prefix[-1] + n)

        def get_sum_i_j(i, j):
            return prefix[j + 1] - prefix[i]

        return helper(0, len(nums) - 1)


so = Solution()
print(so.canSplitArray(nums=[2, 2, 1], m=4))
print(so.canSplitArray([4, 1, 3, 2, 4], 6))
print(so.canSplitArray([1, 1, 1], 3))
print(so.canSplitArray([9, 2, 5, 7, 2], 12))
print(so.canSplitArray([88, 86, 31, 15, 66, 92, 61, 100, 38, 45, 41, 71, 55, 100, 43, 77, 38, 55, 8, 14, 62, 86, 47, 63, 93, 56, 61, 46], 177))
