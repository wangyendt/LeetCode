#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimized Maximum of Products Distributed to Any Store.py 
@time: 2021/11/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)
        while left < right:
            x = (left + right) // 2
            if sum((a + x - 1) // x for a in quantities) > n:
                left = x + 1
            else:
                right = x
        return left
