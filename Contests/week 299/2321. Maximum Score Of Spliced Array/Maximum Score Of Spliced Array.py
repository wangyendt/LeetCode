#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Score Of Spliced Array.py 
@time: 2022/06/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(arr1, arr2):
            """make arr1's sum as large as possible"""
            c = [a2 - a1 for a1, a2 in zip(arr1, arr2)]
            n = len(c)
            dp = [-1e5] * n
            dp[0] = c[0]
            for i in range(n):
                dp[i] = max(dp[i - 1] + c[i], c[i])
            return sum(arr1) + max(dp)

        return max(helper(nums1, nums2), helper(nums2, nums1))
