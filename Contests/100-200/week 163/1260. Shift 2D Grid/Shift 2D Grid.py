#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Shift 2D Grid
@time: 2019/11/19 17:44
"""


class Solution:
    def shiftGrid(self, grid: list(list()), k: int) -> list(list()):
        m, n = len(grid), len(grid[0])
        ret = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                q, r = divmod(j + k, n)
                ret[(i + q) % m][r % n] = grid[i][j]
        return ret


so = Solution()
print(so.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))
print(so.shiftGrid(grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4))
print(so.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=9))
