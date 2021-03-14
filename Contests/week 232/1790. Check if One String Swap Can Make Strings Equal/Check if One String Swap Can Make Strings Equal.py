#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if One String Swap Can Make Strings Equal.py 
@time: 2021/03/14
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        stack = []
        for t1, t2 in zip(s1, s2):
            if t1 != t2:
                stack.append((t1, t2))
        if len(stack) == 0: return True
        if len(stack) == 2:
            if stack[0] == stack[1][::-1]:
                return True
        return False
