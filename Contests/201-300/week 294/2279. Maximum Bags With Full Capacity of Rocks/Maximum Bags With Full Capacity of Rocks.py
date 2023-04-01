#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Bags With Full Capacity of Rocks.py 
@time: 2022/05/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        cur = [c - r for c, r in zip(capacity, rocks)]
        cur.sort(reverse=True)
        ret = 0
        while cur:
            c = cur.pop()
            if c == 0:
                ret += 1
            else:
                additionalRocks -= c
                if additionalRocks >= 0:
                    ret += 1
                else:
                    break
        return ret
