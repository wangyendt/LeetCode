#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Largest Combination With Bitwise AND Greater Than Zero.py 
@time: 2022/05/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *

import numpy as np


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        l = 0
        res = []
        for c in candidates:
            res.append(bin(c)[2:])
            l = max(l, len(res[-1]))
        res = ['0' * (l - len(r)) + r for r in res]
        res = [[int(t) for t in r] for r in res]
        res = np.array(res, dtype=int)
        return max(res.sum(axis=0))
