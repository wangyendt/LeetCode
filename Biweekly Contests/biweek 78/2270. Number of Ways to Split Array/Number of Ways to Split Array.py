#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Ways to Split Array.py 
@time: 2022/05/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = sum(nums)
        l = 0
        r = s
        ret = 0
        for i in range(0, len(nums) - 1):
            l += nums[i]
            r -= nums[i]
            if l >= r:
                ret += 1
        return ret
