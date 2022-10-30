#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Form Array by Concatenating Subarrays of Another Array.py 
@time: 2021/02/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        n = len(groups)
        p = 0
        for i in range(n):
            gr = groups[i]
            for j in range(p, len(nums)):
                if nums[j:j + len(gr)] == gr:
                    p = j + len(gr)
                    break
            else:
                return False
        return True
