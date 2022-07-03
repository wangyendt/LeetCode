#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Wiggle Subsequence.py 
@time: 2022/07/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = None
        ret = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and up != True:
                up = True
                ret += 1
            if nums[i] < nums[i - 1] and up != False:
                up = False
                ret += 1
        return ret
