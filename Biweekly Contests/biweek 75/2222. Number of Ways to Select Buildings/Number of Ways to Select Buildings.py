#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Ways to Select Buildings.py 
@time: 2022/04/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = collections.defaultdict(int)
        for i, t in enumerate(s):
            if t == '0':
                dp['0'] += 1
                dp['10'] += dp['1']
                dp['010'] += dp['01']
            else:
                dp['1'] += 1
                dp['01'] += dp['0']
                dp['101'] += dp['10']
        return dp['101'] + dp['010']
