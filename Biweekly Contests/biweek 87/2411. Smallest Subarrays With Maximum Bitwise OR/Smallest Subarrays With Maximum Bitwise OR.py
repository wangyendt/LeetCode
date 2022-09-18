#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Smallest Subarrays With Maximum Bitwise OR.py 
@time: 2022/09/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        last = [0] * 32
        n = len(nums)
        ret = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    last[j] = i
            ret[i] = max(1, max(last) - i + 1)
        return ret
