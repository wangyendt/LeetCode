#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Score From Removing Stones.py 
@time: 2021/02/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        ret = 0
        while True:
            [a, b, c] = sorted([a, b, c], reverse=True)
            if b <= 0:
                break
            a -= 1
            b -= 1
            ret += 1
            if b == 0 and c == 0: break
        return ret
