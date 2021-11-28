#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Fertile Pyramids in a Land.py 
@time: 2021/11/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import functools
import itertools


class Solution:
    def countPyramids(self, G: List[List[int]]) -> int:
        m, n, ans = len(G), len(G[0]), 0

        @functools.lru_cache(None)
        def dp(i, j, dr):
            if G[i][j] == 1 and 0 <= i + dr < m and j > 0 and j + 1 < n and G[i + dr][j] == 1:
                return min(dp(i + dr, j - 1, dr), dp(i + dr, j + 1, dr)) + 1
            return G[i][j]

        for i, j in itertools.product(range(m), range(n)):
            ans += max(0, dp(i, j, 1) - 1)
            ans += max(0, dp(i, j, -1) - 1)

        return ans
