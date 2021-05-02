#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Distance to the Target Element.py 
@time: 2021/05/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = 1e9
        ret = 0
        for i, n in enumerate(nums):
            if n == target:
                if abs(i - start) < abs(res - start):
                    res = i
                    ret = abs(i - start)
        return ret
