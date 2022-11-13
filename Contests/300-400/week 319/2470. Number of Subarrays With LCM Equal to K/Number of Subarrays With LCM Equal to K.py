#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Subarrays With LCM Equal to K.py 
@time: 2022/11/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
from math import lcm


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0
        for l in range(n):
            m = 1
            for r in range(l, n):
                m = lcm(m, nums[r])
                if m == k:
                    ret += 1
        return ret
