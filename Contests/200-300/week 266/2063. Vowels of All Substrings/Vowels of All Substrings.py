#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Vowels of All Substrings.py 
@time: 2021/11/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        ret = 0
        for i, w in enumerate(word):
            if w in 'aeiou':
                ret += n
                left = i
                right = n - 1 - i
                ret += left * right
        return ret
