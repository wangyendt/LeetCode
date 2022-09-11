#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Optimal Partition of String.py 
@time: 2022/09/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def partitionString(self, s: str) -> int:
        cur = set()
        ret = 1
        for i, t in enumerate(s):
            if t in cur:
                ret += 1
                cur = {t}
            else:
                cur.add(t)
        return ret
