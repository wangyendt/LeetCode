#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Candies Allocated to K Children.py 
@time: 2022/04/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 0, sum(candies) // k
        while left < right:
            mid = (left + right + 1) // 2
            if k > sum(a // mid for a in candies):
                right = mid - 1
            else:
                left = mid
        return left
