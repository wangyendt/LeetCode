#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Subarrays With Fixed Bounds.py 
@time: 2022/10/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_idx = max_idx = bad_idx = -1
        ret = 0
        for i, n in enumerate(nums):
            if not minK <= n <= maxK: bad_idx = i
            if n == minK: min_idx = i
            if n == maxK: max_idx = i
            ret += max(0, min(min_idx, max_idx) - bad_idx)
        return ret


so = Solution()
print(so.countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5))
