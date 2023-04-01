#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Rearranging Fruits.py 
@time: 2023/02/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = collections.defaultdict(int)
        for b in basket1: cnt[b] += 1
        for b in basket2: cnt[b] -= 1
        last = []
        for k, v in cnt.items():
            if v % 2: return -1
            for i in range(abs(v) // 2):
                last.append(k)
        minx = min(min(basket1), min(basket2))
        last.sort()
        ret = 0
        m = len(last)
        for i in range(m // 2):
            ret += min(last[i], minx * 2)
        return ret
