#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Pairs of Interchangeable Rectangles.py 
@time: 2021/09/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res = [r1 / r2 for r1, r2 in rectangles]
        rcnt = collections.Counter(res)
        # print(rcnt)
        ret = 0
        for k, v in rcnt.items():
            ret += v * (v - 1) // 2
        return ret


so = Solution()
print(so.interchangeableRectangles([[4, 8], [3, 6], [10, 20], [15, 30]]))
