#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Merge Strings Alternately.py 
@time: 2021/02/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = ''
        for w1, w2 in zip(word1, word2):
            ret += w1 + w2
        if len(word1) > len(word2):
            ret += word1[len(word2):]
        else:
            ret += word2[len(word1):]
        return ret


so = Solution()
print(so.mergeAlternately('abcd', 'pr'))
