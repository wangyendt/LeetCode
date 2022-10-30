#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum XOR After Operations.py 
@time: 2022/06/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import functools


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return functools.reduce(lambda x, y: x | y, nums)
