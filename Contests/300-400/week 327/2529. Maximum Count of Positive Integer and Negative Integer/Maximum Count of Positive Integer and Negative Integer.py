#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Count of Positive Integer and Negative Integer.py 
@time: 2023/01/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n1 = len([n for n in nums if n > 0])
        n2 = len([n for n in nums if n < 0])
        return max(n1, n2)
