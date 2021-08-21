#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Time to Type Word Using Special Typewriter.py 
@time: 2021/08/21
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minTimeToType(self, word: str) -> int:
        letters = {v: k for k, v in enumerate('abcdefghijklmnopqrstuvwxyz')}
        res = 0
        ret = len(word)
        for w in word:
            ret += min(abs(letters[w] - res) % 26, abs(26 + letters[w] - res) % 26, abs(26 - letters[w] + res) % 26)
            res = letters[w]
        return ret
