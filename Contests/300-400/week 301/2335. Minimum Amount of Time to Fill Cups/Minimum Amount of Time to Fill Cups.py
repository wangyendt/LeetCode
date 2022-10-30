#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Amount of Time to Fill Cups.py 
@time: 2022/07/10
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ret = 0
        while True:
            amount.sort()
            if amount[-1]:
                amount[-1] -= 1
                ret += 1
                if amount[-2]:
                    amount[-2] -= 1
            else:
                break
        return ret
