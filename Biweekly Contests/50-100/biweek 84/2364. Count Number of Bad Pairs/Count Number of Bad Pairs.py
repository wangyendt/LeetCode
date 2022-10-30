#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Number of Bad Pairs.py 
@time: 2022/08/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        nums = [n - i for i, n in enumerate(nums)]
        ret = 0
        for k, v in collections.Counter(nums).items():
            if v > 1:
                ret += v * (v - 1) // 2
        return len(nums) * (len(nums) - 1) // 2 - ret
