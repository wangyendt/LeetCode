#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Substrings That Differ by One Character.py 
@time: 2020/11/01
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        def test(i, j):
            res = pre = cur = 0
            for k in range(min(n - i, m - j)):
                cur += 1
                if s[i + k] != t[j + k]:
                    pre, cur = cur, 0
                res += pre
            return res

        return sum(test(i, 0) for i in range(n)) + sum(test(0, j) for j in range(1, m))
