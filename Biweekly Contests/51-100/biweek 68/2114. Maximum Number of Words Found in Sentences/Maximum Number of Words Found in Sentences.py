#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Number of Words Found in Sentences.py 
@time: 2021/12/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ret = 0
        for s in sentences:
            ret = max(ret, len(s.split(' ')))
        return ret
