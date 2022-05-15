#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Resultant Array After Removing Anagrams.py 
@time: 2022/05/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words) - 1, 0, -1):
            if sorted(words[i]) == sorted(words[i - 1]):
                res.append(i)
        for r in res:
            words.pop(r)
        return words
