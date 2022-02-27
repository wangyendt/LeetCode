#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Steps to Make Two Strings Anagram II.py 
@time: 2022/02/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ret = 0
        cs, ct = collections.Counter(s), collections.Counter(t)
        for l in 'abcdefghijklmnopqrstuvwxyz':
            ret += abs(cs[l] - ct[l])
        return ret
