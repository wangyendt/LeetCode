#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Time to Remove All Cars Containing Illegal Goods.py 
@time: 2022/02/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minimumTime(self, s: str) -> int:
        left, res, n = 0, len(s), len(s)
        for i, c in enumerate(s):
            left = min(left + (c == '1') * 2, i + 1)
            res = min(res, left + n - 1 - i)
        return res
