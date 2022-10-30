#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Cost of Buying Candies With Discount.py 
@time: 2022/01/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        m, r = divmod(len(cost), 3)
        ret = 0
        for i in range(m):
            ret += cost[3 * i] + cost[3 * i + 1]
        if r == 0:
            return ret
        else:
            return ret + sum(cost[-r:])
