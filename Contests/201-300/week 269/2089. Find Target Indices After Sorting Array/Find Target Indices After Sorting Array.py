#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Target Indices After Sorting Array.py 
@time: 2021/11/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ret = []
        nums.sort()
        for i, n in enumerate(nums):
            if n == target:
                ret.append(i)
        return ret
