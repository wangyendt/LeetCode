#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Cost to Make Array Equal.py 
@time: 2022/10/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        total, cnt = sum(cost), 0
        for num, c in arr:
            cnt += c
            if cnt > total // 2:
                target = num
                return sum(c * abs(num - target) for num, c in arr)
