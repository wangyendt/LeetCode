#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Apply Bitwise Operations to Make Strings Equal.py 
@time: 2023/01/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        A, B = set(s), set(target)
        if '1' not in B:
            return '1' not in A
        else:
            return '1' in A
