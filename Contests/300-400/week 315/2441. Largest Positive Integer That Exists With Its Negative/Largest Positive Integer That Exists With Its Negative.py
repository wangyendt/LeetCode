#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Largest Positive Integer That Exists With Its Negative.py 
@time: 2022/10/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        nums_set = set(nums)
        for n in nums[::-1]:
            if -n in nums_set:
                return n
        return -1
