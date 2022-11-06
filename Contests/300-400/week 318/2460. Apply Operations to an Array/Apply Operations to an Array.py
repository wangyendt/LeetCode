#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Apply Operations to an Array.py 
@time: 2022/11/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ptr = 0
        while ptr < len(nums) - 1:
            if nums[ptr] == nums[ptr + 1]:
                nums[ptr] *= 2
                nums[ptr + 1] = 0
            ptr += 1
        n_0 = len([n for n in nums if n == 0])
        ret = []
        for n in nums:
            if n != 0:
                ret.append(n)
        ret.extend([0] * n_0)
        return ret
