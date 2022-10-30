#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Time to Complete Trips.py 
@time: 2022/02/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, int(1e14 + 1)
        while l < r:
            m = (l + r) // 2
            res = 0
            for t in time:
                res += m // t
                if res >= totalTrips:
                    break
            else:
                l = m + 1
                continue
            r = m
        return l


so = Solution()
print(so.minimumTime(time=[1, 2, 3], totalTrips=5))
print(so.minimumTime(time=[2], totalTrips=1))
