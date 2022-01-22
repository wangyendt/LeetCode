#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count the Hidden Sequences.py 
@time: 2022/01/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        res = [0]
        for d in differences:
            res.append(res[-1] + d)
        m, M = min(res), max(res)
        if M - m > upper - lower:
            return 0
        else:
            return (upper - lower) - (M - m) + 1
