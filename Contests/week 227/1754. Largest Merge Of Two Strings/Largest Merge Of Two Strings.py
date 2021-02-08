#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Largest Merge Of Two Strings.py 
@time: 2021/02/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        if word1 >= word2 > '':
            return word1[0] + self.largestMerge(word1[1:], word2)
        if word2 >= word1 > '':
            return word2[0] + self.largestMerge(word1, word2[1:])
        return word1 + word2
