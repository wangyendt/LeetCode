#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Remove Digit From Number to Maximize Result.py 
@time: 2022/05/01
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        occurance = [i for i, n in enumerate(number) if n == digit]
        ret = '0'
        for o in occurance:
            res = number[:o] + number[o + 1:]
            if int(res) > int(ret):
                ret = res
        return ret
