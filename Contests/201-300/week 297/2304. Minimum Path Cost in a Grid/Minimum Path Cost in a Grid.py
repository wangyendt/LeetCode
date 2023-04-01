#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Path Cost in a Grid.py 
@time: 2022/06/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[1e4 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = grid[0][j]
        for i in range(m):
            if i < m - 1:
                for j in range(n):
                    for k in range(n):
                        dp[i + 1][k] = min(dp[i + 1][k], dp[i][j] + moveCost[grid[i][j]][k] + grid[i + 1][k])
                # [print(d) for d in dp]
        return min(dp[-1])


so = Solution()
print(so.minPathCost(grid=[[5, 3], [4, 0], [2, 1]], moveCost=[[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]))
