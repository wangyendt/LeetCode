#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: A Number After a Double Reversal.py 
@time: 2021/12/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s1 = str(num)
        n1 = int(s1[::-1])
        s2 = str(n1)
        n2 = int(s2[::-1])
        return n2 == num
