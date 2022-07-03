#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Increasing Paths in a Grid.py 
@time: 2022/07/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        mod = 10 ** 9 + 7

        def helper(ii, jj, seen):
            if dp[ii][jj] != -1:
                return dp[ii][jj]
            # if not (0<=ii<m and 0<=jj <n):return 0
            res = 0
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = ii + di, jj + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    if grid[ni][nj] > grid[ii][jj]:
                        res += helper(ni, nj, seen)
                    seen.remove((ni, nj))
            if res == 0:
                dp[ii][jj] = 1
            else:
                dp[ii][jj] = res + 1
            return dp[ii][jj]

        for i in range(m):
            for j in range(n):
                if dp[i][j] == -1:
                    helper(i, j, {(i, j)})
                # print(i, j)
                # [print(d) for d in dp]
        # [print(d) for d in dp]
        return sum([sum(d) for d in dp]) % mod


so = Solution()
print(so.countPaths(grid=[[1, 1], [3, 4]]))
