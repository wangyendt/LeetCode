#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Cherry Pickup II
@time: 2020/05/30 23:17
"""

import functools
import sys


class Solution:
    def cherryPickup(self, A: list(list())) -> int:
        m, n = len(A), len(A[0])
        memo = {}

        @functools.lru_cache
        def dfs(i1, j1, i2, j2):
            if (i1, j1, i2, j2) in memo:
                return memo[(i1, j1, i2, j2)]
            if j1 < 0 or j1 > n - 1 or j2 < 0 or j2 > n - 1:
                return -sys.maxsize
            if i1 == m or i2 == m: return 0
            cur = 0
            for x1 in [-1, 0, 1]:
                for x2 in [-1, 0, 1]:
                    cur = max(cur, dfs(i1 + 1, j1 + x1, i2 + 1, j2 + x2))
            if i1 == i2 and j1 == j2:
                ret = cur + A[i1][j1]
            else:
                ret = cur + A[i1][j1] + A[i2][j2]
            memo[(i1, j1, i2, j2)] = ret
            return ret

        return dfs(0, 0, 0, n - 1)


so = Solution()
print(so.cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
print(so.cherryPickup([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                       [1, 0, 2, 3, 0, 0, 6]]))
print(so.cherryPickup([[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]]))
print(so.cherryPickup([[1, 1], [1, 1]]))
