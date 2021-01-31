#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Palindrome Partitioning IV.py 
@time: 2021/01/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import functools


class Solution:
    def checkPartitioning(self, s: str) -> bool:

        @functools.lru_cache(None)
        def help(new_s, n):

            if n == 1: return new_s == new_s[::-1]

            for i in range(len(new_s) - 1):
                if new_s[:i + 1] == new_s[:i + 1][::-1] and help(new_s[i + 1:], n - 1): return True

        return help(s, 3)
