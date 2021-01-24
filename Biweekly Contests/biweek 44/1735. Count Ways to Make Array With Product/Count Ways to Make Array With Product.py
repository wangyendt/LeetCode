#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Ways to Make Array With Product.py 
@time: 2021/01/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import math
import functools
from math import comb


class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
        ress = []
        mod = 10 ** 9 + 7

        def combi(a, b):
            r = 1
            b = min(b, a - b)
            for i in range(b):
                r *= a - i
                r /= i + 1
            return int(r) % mod

        for n, k in queries:
            res = 1
            for p in primes:
                count = 0
                if p > k: break
                while k % p == 0:
                    count += 1
                    k //= p
                res *= combi(count + n - 1, count)
                res %= mod
            if k > 1:
                res = res * n % mod
            ress.append(res)
        return ress
