#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find the Longest Valid Obstacle Course at Each Position.py 
@time: 2021/08/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        mono, res = [], []
        for a in obstacles:
            i = bisect.bisect(mono, a)
            res.append(i + 1)
            if i == len(mono):
                mono.append(0)
            mono[i] = a
        return res


so = Solution()
print(so.longestObstacleCourseAtEachPosition(obstacles=[1, 2, 3, 2]))
print(so.longestObstacleCourseAtEachPosition(obstacles=[2, 2, 1]))
print(so.longestObstacleCourseAtEachPosition(obstacles=[3, 1, 5, 6, 4, 2]))
