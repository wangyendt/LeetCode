#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of Digits of String After Convert.py 
@time: 2021/07/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        d = {k: str(i + 1) for i, k in enumerate('abcdefghijklmnopqrstuvwxyz')}
        res = ''
        for t in s:
            res += d[t]
        for _ in range(k):
            res = str(sum([int(r) for r in res]))
        return int(res)
