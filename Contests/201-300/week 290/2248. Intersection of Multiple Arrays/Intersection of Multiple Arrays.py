#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Intersection of Multiple Arrays.py 
@time: 2022/04/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import functools


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return list(sorted(functools.reduce(lambda x, y: x & y, [set(num) for num in nums])))
