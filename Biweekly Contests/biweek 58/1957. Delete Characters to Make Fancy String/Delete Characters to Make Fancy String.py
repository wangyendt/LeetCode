#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Delete Characters to Make Fancy String.py 
@time: 2021/08/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        res = 1
        ret = ''
        last = '@'
        for i, t in enumerate(s):
            if t == last:
                res += 1
                if res < 3:
                    ret += t
                    # ret += 1
            else:
                ret += t
                res = 1
            last = t
        return ret
