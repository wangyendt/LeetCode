#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Different Integers in a String.py 
@time: 2021/03/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        stack, res = '', []
        for w in word:
            if w.isdigit():
                stack += w
            else:
                if len(stack):
                    res.append(int(stack))
                stack = ''
        if len(stack):
            res.append(int(stack))
        return len(set(res))
