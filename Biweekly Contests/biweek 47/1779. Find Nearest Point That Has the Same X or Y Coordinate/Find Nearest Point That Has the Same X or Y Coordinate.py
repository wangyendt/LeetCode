#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Nearest Point That Has the Same X or Y Coordinate.py 
@time: 2021/03/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import sys


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ret = -1
        res = sys.maxsize
        for i, (ptx, pty) in enumerate(points):
            if x == ptx or y == pty:
                if abs(x - ptx) + abs(y - pty) < res:
                    ret = i
                    res = abs(x - ptx) + abs(y - pty)
        return ret
