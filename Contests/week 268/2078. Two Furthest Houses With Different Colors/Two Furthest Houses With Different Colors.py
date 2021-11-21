#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Two Furthest Houses With Different Colors.py 
@time: 2021/11/21
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ret = 0
        for i in range(n):
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    ret = max(ret, j - i)
        return ret
