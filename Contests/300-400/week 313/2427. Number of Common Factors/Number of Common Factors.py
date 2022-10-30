#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Common Factors.py 
@time: 2022/10/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from math import gcd
import collections
import functools


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c = gcd(a, b)
        d = 2
        res = collections.defaultdict(int)
        while c > 1 and c >= d:
            if c % d == 0:
                res[d] += 1
                c //= d
            else:
                d += 1
        if len(res) == 0:
            return 1
        elif len(res) == 1:
            return list(res.values())[0] + 1
        else:
            return functools.reduce(lambda x, y: x * y, map(lambda t: t + 1, res.values()))


so = Solution()
print(so.commonFactors(a=12, b=6))
print(so.commonFactors(a=25, b=30))
print(so.commonFactors(a=25, b=7))
print(so.commonFactors(885, 885))
