#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Strings That Appear as Substrings in Word.py 
@time: 2021/08/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ret = 0
        for p in patterns:
            if p in word:
                ret += 1
        return ret
