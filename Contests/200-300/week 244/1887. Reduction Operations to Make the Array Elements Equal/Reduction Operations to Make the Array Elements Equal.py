#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Reduction Operations to Make the Array Elements Equal.py 
@time: 2021/06/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        cnter = collections.Counter(nums)
        s = list(sorted(set(nums), reverse=True))
        # print(s)
        ret = 0
        res = 0
        for i, t in enumerate(s):
            if i != len(s) - 1:
                ret += res + cnter[t]
                res += cnter[t]
        return ret
