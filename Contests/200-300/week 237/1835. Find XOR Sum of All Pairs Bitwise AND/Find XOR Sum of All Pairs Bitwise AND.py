#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find XOR Sum of All Pairs Bitwise AND.py 
@time: 2021/04/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import functools
import operator
from typing import *


class Solution:
    def getXORSum(self, A: List[int], B: List[int]):
        return functools.reduce(operator.xor, A) & functools.reduce(operator.xor, B)
