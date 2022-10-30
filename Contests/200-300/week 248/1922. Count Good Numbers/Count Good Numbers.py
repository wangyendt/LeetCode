#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Good Numbers.py 
@time: 2021/07/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import functools


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m = 10 ** 9 + 7
        ne, no = (n + 1) // 2, n // 2

        @functools.lru_cache(None)
        def fast_pow(a, b):
            if b == 0: return 1
            if b == 1: return a
            r1, r2 = fast_pow(a, b // 2) % m, fast_pow(a, b - b // 2) % m
            return (r1 * r2) % m

        return (fast_pow(5, ne) * fast_pow(4, no)) % m


so = Solution()
print(so.countGoodNumbers(10 ** 15))
