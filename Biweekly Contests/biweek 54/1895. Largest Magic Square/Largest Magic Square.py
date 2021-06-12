#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Largest Magic Square
@time: 2021/06/13 00:22
"""

from typing import *


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rs = [[0] + list(accumulate(row)) for row in grid]
        cs = [[0] + list(accumulate(row[c] for row in grid)) for c in range(len(grid[0]))]

        for size in range(min(len(grid), len(grid[0])), 1, -1):
            for j in range(len(grid[0]) - size + 1):
                for i in range(len(grid) - size + 1):
                    s = rs[i][j + size] - rs[i][j]
                    if all(rs[r][j + size] - rs[r][j] == s for r in range(i + 1, i + size)) and \
                            all(cs[c][i + size] - cs[c][i] == s for c in range(j + 1, j + size)) and \
                            sum(grid[x][y] for x, y in zip(range(i, i + size), range(j, j + size))) == s and \
                            sum(grid[x][y] for x, y in zip(range(i + size - 1, i - 1, -1), range(j, j + size))) == s:
                        return size

        return 1
