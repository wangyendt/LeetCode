#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Divide Intervals Into Minimum Number of Groups.py 
@time: 2022/09/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        for i, (start, end) in enumerate(intervals):
            if i == 0:
                res.append(end)
            else:
                idx = bisect.bisect_left(res, start)
                if idx > 0:
                    res[idx - 1:idx] = []
                idx2 = bisect.bisect(res, end)
                res[idx2:idx2] = [end]
        return len(res)


so = Solution()
print(so.minGroups(intervals=[[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]))
print(so.minGroups(intervals=[[1, 3], [5, 6], [8, 10], [11, 13]]))
