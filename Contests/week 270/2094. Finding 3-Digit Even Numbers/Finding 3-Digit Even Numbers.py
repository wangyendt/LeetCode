#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Finding 3-Digit Even Numbers.py 
@time: 2021/12/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ret = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and k != i and digits[i] != 0 and digits[k] % 2 == 0:
                        ret.add(100 * digits[i] + 10 * digits[j] + digits[k])
        return list(sorted(ret))
