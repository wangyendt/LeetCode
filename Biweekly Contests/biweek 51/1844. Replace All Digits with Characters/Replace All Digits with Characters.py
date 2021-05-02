#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Replace All Digits with Characters.py 
@time: 2021/05/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def replaceDigits(self, s: str) -> str:
        ret = ''
        last = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        d = {l: i for i, l in enumerate(letters)}
        for i, t in enumerate(s):
            if i & 1:
                ret += letters[d[last] + int(t)]
            else:
                last = t
                ret += t
        return ret
