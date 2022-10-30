#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find All K-Distant Indices in an Array.py 
@time: 2022/03/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            if n == key:
                res.append(i)
        ret = []
        for i, n in enumerate(nums):
            for r in res:
                if abs(i - r) <= k:
                    ret.append(i)
                    break
        return ret
