#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Divide Array Into Equal Pairs.py 
@time: 2022/03/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnter = collections.Counter(nums)
        for k, v in cnter.items():
            if v & 1:
                return False
        return True
