#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Closed Islands
@time: 2019/11/10 22:10
"""


class Solution:
    def closedIsland(self, grid: list(list())) -> int:
        ret = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n: return False
            if grid[i][j] == 1: return True
            grid[i][j] = 1
            res = True
            for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x, y = i + d[0], j + d[1]
                res &= dfs(x, y)
            return res

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        ret += 1
        return ret


so = Solution()
print(so.closedIsland(
    grid=[[1, 1, 1, 1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0, 1, 1, 0],
          [1, 0, 1, 0, 1, 1, 1, 0],
          [1, 0, 0, 0, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 0]]))
