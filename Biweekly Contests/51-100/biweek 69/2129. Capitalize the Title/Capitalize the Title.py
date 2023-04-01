#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Capitalize the Title.py 
@time: 2022/01/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ts = title.split(' ')
        ret = []
        for t in ts:
            if len(t) <= 2:
                ret.append(t.lower())
            else:
                ret.append(t[0].upper() + t[1:].lower())
        return ' '.join(ret)
