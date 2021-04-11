#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sign of the Product of an Array.py 
@time: 2021/04/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ret = 1
        for n in nums:
            if n == 0:
                return 0
            else:
                if n < 0:
                    ret *= -1
        return ret
