#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Units on a Truck.py 
@time: 2021/01/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        A = sorted(boxTypes, key=lambda x: x[1])
        ret = 0
        while A:
            a, b = A.pop()
            if a >= truckSize:
                ret += truckSize * b
                break
            else:
                ret += a * b
                truckSize -= a
        return ret
