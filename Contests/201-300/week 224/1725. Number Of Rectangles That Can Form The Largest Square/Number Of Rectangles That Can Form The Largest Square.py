#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number Of Rectangles That Can Form The Largest Square.py 
@time: 2021/01/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        a = [min(r) for r in rectangles]
        res = collections.Counter(a)
        return res[max(a)]


so = Solution()
# print(so.countGoodRectangles([[2, 3], [3, 7], [4, 3], [3, 7]]))
print(so.countGoodRectangles([[5, 8], [3, 9], [3, 12]]))
