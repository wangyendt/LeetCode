#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Largest Odd Number in String.py 
@time: 2021/06/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num))[::-1]:
            if int(num[i]) & 1:
                return num[:i + 1]
        return ''
