#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Zero-Filled Subarrays.py 
@time: 2022/07/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        stack = [0]
        for i, num in enumerate(nums):
            if num == 0:
                stack[-1] += 1
            else:
                stack.append(0)
        stack = [s for s in stack if s]
        ret = 0
        for s in stack:
            ret += s * (s + 1) // 2
        return ret
