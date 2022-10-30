#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimize Maximum of Array.py 
@time: 2022/10/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import math


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        cum_sum = 0
        ret = 0
        for i, n in enumerate(nums, start=1):
            cum_sum += n
            ret = max(ret, math.ceil(cum_sum / i))
        return int(ret)


so = Solution()
print(so.minimizeArrayValue(nums=[3, 7, 1, 6]))
print(so.minimizeArrayValue(nums=[3, 7, 1, 7]))
print(so.minimizeArrayValue(nums=[3, 7, 7, 7]))
print(so.minimizeArrayValue([13, 13, 20, 0, 8, 9, 9]))
