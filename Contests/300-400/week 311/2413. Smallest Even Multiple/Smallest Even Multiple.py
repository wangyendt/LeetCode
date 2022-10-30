#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Smallest Even Multiple.py 
@time: 2022/09/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else 2 * n
