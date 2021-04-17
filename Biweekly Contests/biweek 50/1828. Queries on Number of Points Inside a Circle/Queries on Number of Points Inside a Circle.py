#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Queries on Number of Points Inside a Circle.py 
@time: 2021/04/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ret = []
        for x, y, r in queries:
            res = 0
            for px, py in points:
                if (px - x) ** 2 + (py - y) ** 2 <= r ** 2:
                    res += 1
            ret.append(res)
        return ret
