#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Population Year.py 
@time: 2021/05/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        cnter = collections.defaultdict(int)
        for l1, l2 in logs:
            for j in range(l1, l2):
                cnter[j] += 1
        ret = 0
        res = -1
        for i in range(1950, 2051):
            if cnter[i] > res:
                res = cnter[i]
                ret = i
        return ret
