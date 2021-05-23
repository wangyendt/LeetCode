#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Speed to Arrive on Time.py 
@time: 2021/05/23
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour < len(dist) - 1: return -1
        lo = math.ceil(sum(dist) / hour)
        hi = 10 ** 7 + 1
        n = len(dist)
        while lo < hi - 1:
            m = (lo + hi) // 2
            res = 0
            for i, d in enumerate(dist):
                if i < n - 1:
                    res += math.ceil(d / m)
                else:
                    res += d / m
            #     print(res)
            # print(lo, hi, m, res)
            if res >= hour:
                lo = m
            else:
                hi = m - 1
        # print(m)
        for l in [lo, lo + 1]:
            res = 0
            for i, d in enumerate(dist):
                if i < n - 1:
                    res += math.ceil(d / l)
                else:
                    res += d / l
            # print(l, res)
            if res <= hour: return l
        return lo + 2


so = Solution()
print(so.minSpeedOnTime([1, 1, 100000], 2.01))
print(so.minSpeedOnTime(dist=[1, 3, 2], hour=2.7))
print(so.minSpeedOnTime([5, 3, 4, 6, 2, 2, 7], 10.92))
