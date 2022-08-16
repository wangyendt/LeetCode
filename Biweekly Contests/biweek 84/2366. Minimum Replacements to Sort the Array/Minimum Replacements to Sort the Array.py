#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Replacements to Sort the Array.py 
@time: 2022/08/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        x = nums[-1]
        res = 0
        for a in reversed(nums):
            k = (a + x - 1) // x
            x = a // k
            res += k - 1
        return int(res)
