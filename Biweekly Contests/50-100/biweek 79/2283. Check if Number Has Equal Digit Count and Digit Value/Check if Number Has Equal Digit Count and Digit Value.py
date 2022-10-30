#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if Number Has Equal Digit Count and Digit Value.py
@time: 2022/05/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def digitCount(self, num: str) -> bool:
        res = collections.Counter([int(n) for n in num])
        for i, n in enumerate(num):
            if int(n) != res[i]:
                return False
        return True
