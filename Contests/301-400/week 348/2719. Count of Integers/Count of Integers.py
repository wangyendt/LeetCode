#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count of Integers.py 
@time: 2023/06/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import functools


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod = 10 ** 9 + 7

        def f(s, v):
            n = len(s)
            res = sum(map(int, s)) == v
            for i, c in enumerate(s):
                c = int(c)
                for c2 in range(min(c, v + 1)):
                    res += split(v - c2, n - i - 1)
                v -= c
            return res

        @functools.lru_cache(None)
        def split(v, k):
            if v == 0: return 1
            if v > 9 * k or v < 0 or k == 0: return 0
            return sum(split(v - vv, k - 1) for vv in range(10)) % mod

        num1_1 = str(int(num1) - 1)
        return sum(f(num2, v) - f(num1_1, v) for v in range(min_sum, max_sum + 1)) % mod


so = Solution()
print(so.count(num1="1", num2="12", min_sum=1, max_sum=8))
