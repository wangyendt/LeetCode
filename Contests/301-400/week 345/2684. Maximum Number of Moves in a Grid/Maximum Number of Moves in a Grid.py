"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Maximum Number of Moves in a Grid.py
@time: 20230514
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""
import functools
from typing import *


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n, dirs = len(grid), len(grid[0]), [(0, 1), (1, 1), (-1, 1)]

        @functools.lru_cache(None)
        def dp(i, j):
            ans = 0
            for x, y in dirs:
                ni, nj = i + x, j + y
                if 0 <= ni < m and nj < n and grid[i][j] < grid[ni][nj]:
                    ans = max(ans, 1 + dp(ni, nj))
            return ans

        return max(dp(i, 0) for i in range(m))
