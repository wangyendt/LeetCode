#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Earnings From Taxi.py 
@time: 2021/09/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        rides.sort(key=lambda x: x[1])
        # print(rides)
        ret = 0
        last = 0
        for i, r in enumerate(rides):
            s, e, p = r
            for j in range(last, e): dp[j] = dp[last]
            last = e
            # print(f'{i + 1=}, {s=}, {e=}, {p=}, {dp[s] + e - s + p=}, {dp[i]=}, {dp[s]=},{dp=}')
            dp[e] = max(ret, dp[s] + e - s + p)
            ret = max(ret, dp[e])
        # print(dp)
        return ret


so = Solution()
print(so.maxTaxiEarnings(n=5, rides=[[2, 5, 4], [1, 5, 1]]))
print(so.maxTaxiEarnings(n=20, rides=[[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]))
print(so.maxTaxiEarnings(5, [[2, 3, 4], [4, 5, 1]]))
