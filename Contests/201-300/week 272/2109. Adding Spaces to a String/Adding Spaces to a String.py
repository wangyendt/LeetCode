#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Adding Spaces to a String.py 
@time: 2021/12/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.sort()
        res = []
        pre = 0
        for sp in spaces:
            res.append(s[pre:sp])
            pre = sp
        res.append(s[pre:])
        return ' '.join(res)
