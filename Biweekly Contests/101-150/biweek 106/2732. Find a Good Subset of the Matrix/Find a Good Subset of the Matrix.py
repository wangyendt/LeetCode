"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find a Good Subset of the Matrix.py
@time: 20230611
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        vec = []
        for row in grid:
            num = 0
            for j in range(n):
                num |= (row[j] << j)
            vec.append(num)
        for i in range(m):
            if vec[i] == 0: return [i]
            for j in range(i + 1, m):
                if vec[i] & vec[j] == 0: return [i, j]
        return []
