#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Smallest Index With Equal Value.py 
@time: 2021/10/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i % 10 == n:
                return i
        return -1
