#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Longest Substring Of All Vowels in Order.py 
@time: 2021/04/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ret = 0
        res = 0
        kind = set()
        for i in range(len(word)):
            if i == 0:
                res = 1
                kind.add(word[i])
            else:
                if word[i] >= word[i - 1]:
                    res += 1
                    kind.add(word[i])
                    if len(kind) == 5:
                        ret = max(ret, res)
                else:
                    res = 1
                    kind = set(word[i])
        return ret
