#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Widest Vertical Area Between Two Points Containing No Points.py 
@time: 2020/11/01
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted([pt[0] for pt in points])
        return max(x[i + 1] - x[i] for i in range(len(x) - 1))


so = Solution()
print(so.maxWidthOfVerticalArea(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
