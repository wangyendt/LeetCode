#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximize Win From Two Segments.py 
@time: 2023/02/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        best = [0] * (n + 1)  # best segment after >= i
        res = 0
        for i in range(n - 1, -1, -1):  # curr seg start at ith
            e = bisect.bisect_right(prizePositions, prizePositions[i] + k)  # take maximum as possible
            res = max(res, e - i + best[e])  # maximize the segments by curr seg + next segment after >= e
            best[i] = max(best[i + 1], e - i)  # track the best segment
        return res
