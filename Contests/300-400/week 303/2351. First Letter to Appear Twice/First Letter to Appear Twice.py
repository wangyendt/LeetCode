#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: First Letter to Appear Twice.py 
@time: 2022/07/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        cnt = collections.defaultdict(int)
        for i, t in enumerate(s):
            cnt[t] += 1
            if cnt[t] == 2:
                return t
