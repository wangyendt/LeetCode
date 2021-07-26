#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Largest Number After Mutating Substring.py 
@time: 2021/07/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)
        on = False
        for i, ch in enumerate(num):
            ref = str(change[int(ch)])
            if ch < ref:
                on = True
                num[i] = ref
            elif ch > ref:
                if on: break
        return "".join(num)
