#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Build Array from Permutation.py 
@time: 2021/07/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ret = []
        for n in nums:
            ret.append(nums[n])
        return ret
