#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if Point Is Reachable.py 
@time: 2023/01/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from math import gcd


class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        g = gcd(targetX, targetY)
        return g & (g - 1) == 0
