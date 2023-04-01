#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Substrings of Size Three with Distinct Characters.py 
@time: 2021/05/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ret = 0
        for i in range(len(s) - 2):
            t = s[i:i + 3]
            if len(set(t)) == 3:
                ret += 1
        return ret
