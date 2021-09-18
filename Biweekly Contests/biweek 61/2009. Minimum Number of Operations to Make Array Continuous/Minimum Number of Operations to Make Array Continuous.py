#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Operations to Make Array Continuous.py 
@time: 2021/09/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        arr = sorted(set(nums))
        result = float('inf')
        for i, num in enumerate(arr):
            j = bisect.bisect_right(arr, num + len(nums) - 1)
            result = min(result, len(nums) - (j - i))
        return result


so = Solution()
print(so.minOperations([4, 2, 5, 3]))
print(so.minOperations([1, 2, 3, 5, 6]))
print(so.minOperations([1, 10, 100, 1000]))
