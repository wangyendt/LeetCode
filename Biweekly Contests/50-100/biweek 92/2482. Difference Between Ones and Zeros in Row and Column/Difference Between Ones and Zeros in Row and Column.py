"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Difference Between Ones and Zeros in Row and Column.py
@time: 20221126
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ones_row = [0] * m
        ones_col = [0] * n
        zeros_row = [0] * m
        zeros_col = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zeros_row[i] += 1
                else:
                    ones_row[i] += 1
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 0:
                    zeros_col[j] += 1
                else:
                    ones_col[j] += 1
        ret = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ret[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]
        return ret
