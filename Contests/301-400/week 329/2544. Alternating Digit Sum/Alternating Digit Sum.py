#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Alternating Digit Sum.py 
@time: 2023/01/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        ret = 0
        res = 1
        for i, t in enumerate(s):
            ret += res * int(t)
            res *= -1
        return ret
