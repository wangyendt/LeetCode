#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Greatest English Letter in Upper and Lower Case.py 
@time: 2022/06/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def greatestLetter(self, s: str) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        s_set = set(s)
        for l in letters:
            if l in s_set and l.upper() in s_set:
                res.append(l)
        if res:
            return ''.join(sorted(res)[-1].upper())
        return ''
