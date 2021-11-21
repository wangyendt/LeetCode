#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Watering Plants.py 
@time: 2021/11/21
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cur = capacity
        ret = 0
        for i, p in enumerate(plants):
            if cur >= p:
                cur -= p
                ret += 1
            else:
                cur = capacity - p
                ret += i * 2 + 1
        return ret
