#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Ice Cream Bars.py 
@time: 2021/04/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = [c for c in costs if c <= coins]
        costs.sort()
        ret = 0
        res = 0
        for c in costs:
            if res + c <= coins:
                ret += 1
                res += c
            else:
                break
        return ret
