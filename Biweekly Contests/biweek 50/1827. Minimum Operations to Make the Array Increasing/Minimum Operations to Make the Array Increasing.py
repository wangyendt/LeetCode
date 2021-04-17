#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Operations to Make the Array Increasing.py 
@time: 2021/04/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        ret = 0
        for n in nums:
            if res >= n:
                ret += res + 1 - n
                res += 1
            else:
                res = n
        return ret
