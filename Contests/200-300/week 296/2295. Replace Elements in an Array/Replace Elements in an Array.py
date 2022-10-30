#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Replace Elements in an Array.py 
@time: 2022/06/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        res = collections.defaultdict(int)
        for i, n in enumerate(nums):
            res[n] = i
        for op1, op2 in operations:
            nums[res[op1]] = op2
            res[op2] = res[op1]
            res[op1] = -1
        return nums
