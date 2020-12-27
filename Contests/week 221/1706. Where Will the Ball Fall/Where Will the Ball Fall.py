#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Where Will the Ball Fall
@time: 2020/12/27 12:05
"""

from typing import *


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        valid = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if j + 1 < n and grid[i][j + 1] == 1:
                        valid[i][j] = j + 1
                    else:
                        valid[i][j] = -10
                else:
                    if j - 1 >= 0 and grid[i][j - 1] == -1:
                        valid[i][j] = j - 1
                    else:
                        valid[i][j] = -10
        ret = []
        for j in range(n):
            k = j
            for i in range(m):
                if valid[i][k] == -10:
                    break
                else:
                    k = valid[i][k]
            else:
                ret.append(k)
                continue
            ret.append(-1)
        return ret
