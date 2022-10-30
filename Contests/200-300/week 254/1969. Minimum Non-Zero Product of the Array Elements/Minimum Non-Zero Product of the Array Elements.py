#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Non-Zero Product of the Array Elements.py 
@time: 2021/08/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1: return 1
        if p == 2: return 6
        q = 2 ** p - 1
        r = 2 ** (p - 1) - 1
        # print(r)
        mod = 10 ** 9 + 7
        return (q * pow(q - 1, r, mod)) % mod


so = Solution()
print(so.minNonZeroProduct(60))
