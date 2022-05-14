#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find the K-Beauty of a Number.py 
@time: 2022/05/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s_num = str(num)
        ret = 0
        for i in range(k, len(s_num) + 1):
            res = int(s_num[i - k:i])
            if res != 0 and num % res == 0:
                ret += 1
        return ret
