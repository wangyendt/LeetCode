#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Counting Words With a Given Prefix.py 
@time: 2022/02/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ret = 0
        for w in words:
            if w.startswith(pref):
                ret += 1
        return ret
