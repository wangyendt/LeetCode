#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Operations to Obtain Zero.py 
@time: 2022/02/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ret = 0
        if num1 == 0 or num2 == 0: return 0
        while True:
            if num1 < num2:
                num1, num2 = num2, num1
            m, r = divmod(num1, num2)
            ret += m
            num1 = r
            if num1 == 0:
                break
        return ret
