#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Distinct Averages.py 
@time: 2022/11/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s = set()
        for i in range(len(nums) // 2):
            s.add((nums[i] + nums[~i]) / 2)
        return len(s)
