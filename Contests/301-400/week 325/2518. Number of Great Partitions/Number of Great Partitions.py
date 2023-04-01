#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Great Partitions.py 
@time: 2022/12/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < k * 2: return 0
        mod = 10 ** 9 + 7
        dp = [1] + [0] * (k - 1)
        for a in nums:
            for i in range(k - 1 - a, -1, -1):
                dp[i + a] += dp[i]
        return (pow(2, len(nums), mod) - sum(dp) * 2) % mod
