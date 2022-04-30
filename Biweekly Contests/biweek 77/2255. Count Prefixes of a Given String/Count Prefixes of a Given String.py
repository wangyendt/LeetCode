#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Prefixes of a Given String.py 
@time: 2022/04/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ret = 0
        for w in words:
            if s.startswith(w):
                ret += 1
        return ret
