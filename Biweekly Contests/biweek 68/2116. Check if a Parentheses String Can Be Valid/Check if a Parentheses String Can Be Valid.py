#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if a Parentheses String Can Be Valid.py 
@time: 2021/12/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1: return False
        tot = op = cl = 0  # tot -> Total variable brackets, op -> Open, cl -> Closed
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                tot += 1
            elif s[i] == '(':
                op += 1
            elif s[i] == ')':
                cl += 1
            if tot - op + cl < 0: return False
        tot = op = cl = 0
        for i in range(len(s)):
            if locked[i] == '0':
                tot += 1
            elif s[i] == '(':
                op += 1
            elif s[i] == ')':
                cl += 1
            if tot + op - cl < 0: return False
        return True
