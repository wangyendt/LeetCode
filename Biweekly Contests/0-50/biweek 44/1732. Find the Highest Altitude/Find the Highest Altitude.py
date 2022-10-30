#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find the Highest Altitude.py 
@time: 2021/01/23
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ret = 0
        s = 0
        for g in gain:
            s += g
            ret = max(ret, s)
        return ret
