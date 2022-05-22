#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Percentage of Letter in String.py 
@time: 2022/05/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(collections.Counter(s)[letter] * 100 / len(s))
