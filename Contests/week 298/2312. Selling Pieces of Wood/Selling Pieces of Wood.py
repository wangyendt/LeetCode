#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Selling Pieces of Wood.py 
@time: 2022/06/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for w, h, p in prices:
            dp[w][h] = p
        for w in range(1, m + 1):
            for h in range(1, n + 1):
                for a in range(1, w // 2 + 1):
                    dp[w][h] = max(dp[w][h], dp[a][h] + dp[w - a][h])
                for a in range(1, h // 2 + 1):
                    dp[w][h] = max(dp[w][h], dp[w][a] + dp[w][h - a])
        return dp[m][n]
