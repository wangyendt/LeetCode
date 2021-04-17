#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Operations to Make String Sorted.py 
@time: 2021/04/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import functools


class Solution:
    @functools.lru_cache(None)
    def f(self, i):
        return 1 if i <= 1 else (self.f(i - 1) * i) % (10 ** 9 + 7)

    def makeStringSorted(self, s):
        N, n, out = 10 ** 9 + 7, len(s), 0
        cnt = [0] * 26
        for i in range(n - 1, -1, -1):
            ind = ord(s[i]) - ord("a")
            cnt[ind] += 1
            ans = sum(cnt[:ind]) * self.f(n - i - 1)
            for i in range(26):
                ans = ans * pow(self.f(cnt[i]), N - 2, N) % N
            out += ans
        return out % N
