#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Greatest Common Divisor of Array.py 
@time: 2021/08/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if a < b: a, b = b, a
            while b:
                a, b = b, a % b
            return a

        return gcd(min(nums), max(nums))
