#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Second Largest Digit in a String.py 
@time: 2021/03/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def secondHighest(self, s: str) -> int:
        res = set()
        for t in s:
            if t in '0123456789':
                res.add(int(t))
        res = sorted(list(res))
        if len(res) < 2:
            return -1
        return res[-2]
