#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: K Radius Subarray Averages.py 
@time: 2021/11/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if 2 * k + 1 > n:
            return [-1] * n
        ret = [-1] * n
        s = 0
        for i, a in enumerate(nums):
            s += a
            if i >= 2 * k:
                ret[i - k] = s // (2 * k + 1)
                s -= nums[i - 2 * k]
        return ret
