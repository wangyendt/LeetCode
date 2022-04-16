#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Closest Number to Zero.py 
@time: 2022/04/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ret = 1e100
        for n in nums:
            if abs(n) < abs(ret):
                ret = n
            elif abs(n) == abs(ret):
                ret = max(ret, n)
        return ret
