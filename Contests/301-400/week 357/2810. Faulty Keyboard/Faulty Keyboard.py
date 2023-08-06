#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Faulty Keyboard.py 
@time: 2023/08/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def finalString(self, s: str) -> str:
        stack = []
        for t in s:
            if t != 'i':
                stack.append(t)
            else:
                stack = stack[::-1]
        return ''.join(stack)
