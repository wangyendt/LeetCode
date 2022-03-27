#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Value of K Coins From Piles.py 
@time: 2022/03/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import functools


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @functools.lru_cache(None)
        def dp(i, k):
            if k == 0 or i == len(piles): return 0
            res, cur = dp(i + 1, k), 0
            for j in range(min(len(piles[i]), k)):
                cur += piles[i][j]
                res = max(res, cur + dp(i + 1, k - j - 1))
            return res

        return dp(0, k)
