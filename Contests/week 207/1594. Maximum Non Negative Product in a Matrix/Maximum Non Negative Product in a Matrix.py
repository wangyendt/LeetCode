#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Non Negative Product in a Matrix
@time: 2020/09/20 18:40
"""

from typing import *


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp1 = [[1 for _ in range(n + 1)] for _ in range(m + 1)]
        dp2 = [[1 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                r1, r2, r3, r4 = dp1[i - 1][j], dp1[i][j - 1], dp2[i - 1][j], dp2[i][j - 1]
                A = [r * grid[i - 1][j - 1] for r in (r1, r2, r3, r4)]
                if i == 1:
                    dp1[i][j] = A[1]
                    dp2[i][j] = A[3]
                elif j == 1:
                    dp1[i][j] = A[0]
                    dp2[i][j] = A[2]
                else:
                    mn, mx = min(A), max(A)
                    dp1[i][j] = mx
                    dp2[i][j] = mn
        return dp1[-1][-1] % (10 ** 9 + 7) if dp1[-1][-1] >= 0 else -1


so = Solution()
print(so.maxProductPath(grid=[[-1, -2, -3],
                              [-2, -3, -3],
                              [-3, -3, -2]]))
