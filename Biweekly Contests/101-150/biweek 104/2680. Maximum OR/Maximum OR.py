#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum OR.py 
@time: 2023/05/14
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        cur = 0
        saved = 0
        for num in nums:
            saved |= num & cur
            cur |= num

        max_num = 0

        for num in nums:
            max_num = max(max_num, saved | (cur & ~num) | num << k)
        return max_num
