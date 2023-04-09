#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Convert an Array Into a 2D Array With Conditions.py 
@time: 2023/04/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = collections.defaultdict(int)
        ret = []
        for i, num in enumerate(nums):
            res[num] += 1
            if res[num] > len(ret):
                ret.append([])
            ret[res[num] - 1].append(num)
        return ret
