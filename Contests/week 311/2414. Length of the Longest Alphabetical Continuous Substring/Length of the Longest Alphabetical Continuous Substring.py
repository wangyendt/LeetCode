#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Length of the Longest Alphabetical Continuous Substring.py 
@time: 2022/09/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ret = res = 1
        last = -1
        for i, t in enumerate(s):
            if ord(t) - last == 1:
                res += 1
            else:
                res = 1
            last = ord(t)
            ret = max(res, ret)
        return ret
