#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sorting the Sentence.py 
@time: 2021/05/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        res = []
        for t in s.split(' '):
            res.append((t[:-1], int(t[-1])))
        res.sort(key=lambda x: x[1])
        return ' '.join([r[0] for r in res])
