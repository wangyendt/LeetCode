#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Sideway Jumps.py 
@time: 2021/04/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minSideJumps(self, A: List[int]) -> int:
        dp = [1, 0, 1]
        for a in A:
            if a:
                dp[a - 1] = float('inf')
            for i in range(3):
                if a != i + 1:
                    dp[i] = min(dp[i], dp[(i + 1) % 3] + 1, dp[(i + 2) % 3] + 1)
        return min(dp)
