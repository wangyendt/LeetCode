#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find the Longest Balanced Substring of a Binary String.py 
@time: 2023/04/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if len(sub) % 2 == 0 and all(s == '0' for s in sub[:len(sub) // 2]) and all(s == '1' for s in sub[len(sub) // 2:]):
                    ret = max(ret, len(sub))
        return ret
