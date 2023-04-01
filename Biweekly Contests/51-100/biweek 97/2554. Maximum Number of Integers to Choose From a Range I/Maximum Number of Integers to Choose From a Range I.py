#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Number of Integers to Choose From a Range I.py 
@time: 2023/02/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ret = 0
        banned = set(banned)
        res = 0
        for i in range(1, n + 1):
            if i in banned:
                continue
            res += i
            if res > maxSum:
                return ret
            ret += 1
        return ret
