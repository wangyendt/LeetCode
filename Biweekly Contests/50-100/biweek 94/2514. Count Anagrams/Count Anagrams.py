#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Anagrams.py 
@time: 2022/12/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
from math import factorial


class Solution:
    def countAnagrams(self, s: str) -> int:
        mod = 10 ** 9 + 7

        def get_comb(ss: str):
            cnter = collections.Counter(ss)
            ret = factorial(len(ss))
            for k, v in cnter.items():
                if v > 1:
                    ret //= factorial(v)
            return ret % mod

        ret = 1
        for t in s.split(' '):
            ret = (ret * get_comb(t)) % mod
        return ret
