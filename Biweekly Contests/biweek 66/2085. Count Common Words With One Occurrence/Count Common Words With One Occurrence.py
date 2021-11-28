#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Common Words With One Occurrence.py 
@time: 2021/11/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1, cnt2 = collections.Counter(words1), collections.Counter(words2)
        ret = 0
        for k, v in cnt1.items():
            if v == 1:
                if k in cnt2 and cnt2[k] == 1:
                    ret += 1
        return ret
