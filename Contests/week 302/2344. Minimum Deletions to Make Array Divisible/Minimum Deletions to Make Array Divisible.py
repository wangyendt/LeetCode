#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Deletions to Make Array Divisible.py 
@time: 2022/07/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import math
from typing import *


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        common_divs = numsDivide[0]
        for i in range(1, len(numsDivide)):
            common_divs = math.gcd(common_divs, numsDivide[i])
        nums.sort()
        for i, num in enumerate(nums):
            if common_divs % num == 0:
                return i
        return -1
