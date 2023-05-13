#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Power of Heroes.py 
@time: 2023/05/14
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        mod, pre, res = 10 ** 9 + 7, 0, 0
        for x in sorted(nums):
            res = (res + x * x * x + x * x * pre) % mod
            pre = (pre * 2 + x) % mod
        return res
