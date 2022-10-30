#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Rearrange Characters to Make Target String.py 
@time: 2022/05/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ret = 1e10
        res = collections.Counter(s)
        for k, v in collections.Counter(target).items():
            ret = min(ret, res[k] // v)
        if ret == 1e10:
            ret = 0
        return ret
