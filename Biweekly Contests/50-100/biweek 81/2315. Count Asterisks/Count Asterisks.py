#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Asterisks.py 
@time: 2022/06/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        ret = 0
        b = False
        for i, t in enumerate(s):
            if t == '|':
                b = not b
            if not b and t == '*':
                ret += 1
        return ret
