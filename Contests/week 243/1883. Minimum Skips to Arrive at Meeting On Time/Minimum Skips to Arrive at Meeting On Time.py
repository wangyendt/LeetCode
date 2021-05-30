#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Skips to Arrive at Meeting On Time.py 
@time: 2021/05/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        def roundup(d, s=speed):
            if d % s == 0:
                return d
            else:
                return d + (s - d % s)

        n = len(dist)
        dp = [[-1] * n for _ in range(n)]
        dp[0][0] = dist[0]
        for i in range(1, n):
            dp[i][0] = roundup(dp[i - 1][0]) + dist[i]
            for j in range(1, i):
                dp[i][j] = min(roundup(dp[i - 1][j]), dp[i - 1][j - 1]) + dist[i]
            dp[i][i] = dp[i - 1][i - 1] + dist[i]
        for k in range(n):
            if dp[-1][k] / speed <= hoursBefore:
                return k
        return -1
