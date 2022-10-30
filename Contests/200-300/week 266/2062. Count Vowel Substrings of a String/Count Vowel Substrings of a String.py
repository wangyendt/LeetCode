#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Vowel Substrings of a String.py 
@time: 2021/11/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        ret = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                ww = word[i:j]
                if all(l in ww for l in 'aeiou') and not any(l in ww for l in 'bcdfghjklmnpqrstvwxyz'):
                    ret += 1
        return ret
