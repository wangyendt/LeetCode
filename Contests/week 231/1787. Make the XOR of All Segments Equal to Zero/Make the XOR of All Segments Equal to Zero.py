#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Make the XOR of All Segments Equal to Zero.py 
@time: 2021/03/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:

        LIMIT = 2 ** 10
        mrr = [[0 for _ in range(LIMIT)]
               for _ in range(k)]
        for i, x in enumerate(nums):
            mrr[i % k][x] += 1

        dp = [-2000 for _ in range(LIMIT)]
        dp[0] = 0
        for row in mrr:
            maxprev = max(dp)
            new_dp = [maxprev for _ in range(LIMIT)]
            for i, cnt in enumerate(row):
                if cnt == 0:
                    continue
                for j, prev in enumerate(dp):
                    new_dp[i ^ j] = max(new_dp[i ^ j],
                                        prev + cnt)
            dp = new_dp

        return len(nums) - new_dp[0]
