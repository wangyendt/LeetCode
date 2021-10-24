#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Next Greater Numerically Balanced Number.py 
@time: 2021/10/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n += 1
        while True:
            sn = str(n)
            for i, v in collections.Counter(sn).items():
                if int(i) != v:
                    break
            else:
                return n
            n += 1
