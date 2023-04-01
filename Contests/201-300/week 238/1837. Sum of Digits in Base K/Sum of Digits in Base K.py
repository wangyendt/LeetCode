#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of Digits in Base K.py 
@time: 2021/04/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def f(n: int, x: int):
            a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            b = []
            while True:
                s, y = divmod(n, x)
                b = b + [y]
                if s == 0:
                    break
                n = s
            b.reverse()
            for i in b:
                yield a[i]

        ret = 0
        for a in f(n, k):
            ret += int(a)
        return ret
