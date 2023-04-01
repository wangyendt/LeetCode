#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Integers With Even Digit Sum.py 
@time: 2022/02/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def countEven(self, num: int) -> int:
        ret = 0
        for i in range(2, num + 1):
            if sum([int(j) for j in str(i)]) % 2 == 0:
                ret += 1
        return ret
