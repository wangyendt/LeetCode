#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Last Day Where You Can Still Cross.py 
@time: 2021/08/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import itertools
import sys
from typing import *

sys.path.append('../../..')
from Tools.UnionFindSet import *


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        m, n = row, col
        uf = UnionFind(m * n + 2)
        grid = [[0] * n for _ in range(m)]
        neibs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        C = [(x - 1, y - 1) for x, y in cells]

        def index(x, y):
            return x * n + y + 1

        for x, y in C: grid[x][y] = 1

        for x, y in itertools.product(range(m), range(n)):
            if grid[x][y] == 1: continue
            i = index(x, y)
            if x == 0: uf.union(i, 0)
            if x == n - 1: uf.union(i, m * n + 1)
            for dx, dy in neibs:
                if 0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] == 0:
                    uf.union(i, index(x + dx, y + dy))

        for i in range(len(C) - 1, -1, -1):
            x, y = C[i][0], C[i][1]

            grid[x][y] = 0
            for dx, dy in neibs:
                ind = index(x + dx, y + dy)
                if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n and grid[x + dx][y + dy] == 0:
                    uf.union(ind, index(x, y))
            if x == 0:
                uf.union(0, index(x, y))
            if x == m - 1:
                uf.union(m * n + 1, index(x, y))

            if uf.find(0) == uf.find(m * n + 1):
                return i


so = Solution()
print(so.latestDayToCross(row=3, col=3, cells=[[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]))
print(so.latestDayToCross(6,
                          2,
                          [[4, 2], [6, 2], [2, 1], [4, 1], [6, 1], [3, 1], [2, 2], [3, 2], [1, 1], [5, 1], [5, 2],
                           [1, 2]]))
