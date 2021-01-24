#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Building Boxes.py 
@time: 2021/01/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minimumBoxes(self, n: int) -> int:
        x = int((n * 6) ** (1. / 3)) - 1
        n -= x * (x + 1) * (x + 2) / 6
        y = int((n * 2 + 0.25) ** 0.5 + 0.49999999)
        return x * (x + 1) // 2 + y
