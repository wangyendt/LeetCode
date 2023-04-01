#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Stamping the Grid.py 
@time: 2022/01/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import itertools


class Solution:
    def possibleToStamp(self, grid: List[List[int]], H: int, W: int) -> bool:
        def acc_2d(grid):
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for c, r in itertools.product(range(n), range(m)):
                dp[r + 1][c + 1] = dp[r + 1][c] + dp[r][c + 1] - dp[r][c] + grid[r][c]
            return dp

        def sumRegion(r1, c1, r2, c2):
            return dp[r2 + 1][c2 + 1] - dp[r1][c2 + 1] - dp[r2 + 1][c1] + dp[r1][c1]

        m, n = len(grid), len(grid[0])
        dp = acc_2d(grid)

        diff = [[0] * (n + 1) for _ in range(m + 1)]
        for c in range(n - W + 1):
            for r in range(m - H + 1):
                if sumRegion(r, c, r + H - 1, c + W - 1) == 0:
                    diff[r][c] += 1
                    diff[r][c + W] -= 1
                    diff[r + H][c] -= 1
                    diff[r + H][c + W] += 1

        dp2 = acc_2d(diff)
        for c, r in itertools.product(range(n), range(m)):
            if dp2[r + 1][c + 1] == 0 and grid[r][c] != 1: return False

        return True
