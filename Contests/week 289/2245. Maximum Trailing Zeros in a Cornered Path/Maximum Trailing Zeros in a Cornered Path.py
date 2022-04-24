#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Trailing Zeros in a Cornered Path.py 
@time: 2022/04/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import itertools
from typing import *


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def helper(A: List[List[int]]):
            m, n = len(A), len(A[0])
            left, right, up, down = [], [], [], []
            for i in range(m):
                left.append(list(itertools.accumulate(A[i], lambda x, y: x + y)))
                right.append(list(itertools.accumulate(A[i][::-1], lambda x, y: x + y))[::-1])
            for j in range(n):
                up.append(list(itertools.accumulate([A[i][j] for i in range(m)], lambda x, y: x + y)))
                down.append(list(itertools.accumulate([A[i][j] for i in range(m)[::-1]], lambda x, y: x + y))[::-1])
            up = list(map(list, zip(*up)))
            down = list(map(list, zip(*down)))
            return left, right, up, down

        m, n = len(grid), len(grid[0])
        if m == 1:
            res2, res5 = 0, 0
            for g in grid[0]:
                while g:
                    if g % 2 == 0:
                        res2 += 1
                        g //= 2
                    elif g % 5 == 0:
                        res5 += 1
                        g //= 5
                    else:
                        break
            return min(res2, res5)
        if n == 1:
            res2, res5 = 0, 0
            for gs in grid:
                g = gs[0]
                while g:
                    if g % 2 == 0:
                        res2 += 1
                        g //= 2
                    elif g % 5 == 0:
                        res5 += 1
                        g //= 5
                    else:
                        break
            return min(res2, res5)
        G2 = [[0 for _ in range(n)] for _ in range(m)]
        G5 = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in itertools.product(range(m), range(n)):
            g = grid[i][j]
            while g:
                if g % 2 == 0:
                    G2[i][j] += 1
                    g //= 2
                elif g % 5 == 0:
                    G5[i][j] += 1
                    g //= 5
                else:
                    break
        l2, r2, u2, d2 = helper(G2)
        l5, r5, u5, d5 = helper(G5)
        ret = 0
        for i, j in itertools.product(range(m), range(n)):
            if i == 0:
                if j == 0:
                    ret = max(ret, min(d2[i][j] + r2[i][j + 1], d5[i][j] + r5[i][j + 1]))
                elif j == n - 1:
                    ret = max(ret, min(d2[i][j] + l2[i][j - 1], d5[i][j] + l5[i][j - 1]))
                else:
                    ret = max(
                        ret,
                        min(d2[i][j] + l2[i][j - 1], d5[i][j] + l5[i][j - 1]),
                        min(d2[i][j] + r2[i][j + 1], d5[i][j] + r5[i][j + 1])
                    )
            elif i == m - 1:
                if j == 0:
                    ret = max(ret, min(u2[i][j] + r2[i][j + 1], u5[i][j] + r5[i][j + 1]))
                elif j == n - 1:
                    ret = max(ret, min(u2[i][j] + l2[i][j - 1], u5[i][j] + l5[i][j - 1]))
                else:
                    ret = max(
                        ret,
                        min(u2[i][j] + l2[i][j - 1], u5[i][j] + l5[i][j - 1]),
                        min(u2[i][j] + r2[i][j + 1], u5[i][j] + r5[i][j + 1])
                    )
            else:
                if j == 0:
                    ret = max(
                        ret,
                        min(u2[i][j] + r2[i][j + 1], u5[i][j] + r5[i][j + 1]),
                        min(d2[i][j] + r2[i][j + 1], d5[i][j] + r5[i][j + 1])
                    )
                elif j == n - 1:
                    ret = max(
                        ret,
                        min(u2[i][j] + l2[i][j - 1], u5[i][j] + l5[i][j - 1]),
                        min(d2[i][j] + l2[i][j - 1], d5[i][j] + l5[i][j - 1]),
                    )
                else:
                    ret = max(
                        ret,
                        min(u2[i][j] + l2[i][j - 1], u5[i][j] + l5[i][j - 1]),
                        min(u2[i][j] + r2[i][j + 1], u5[i][j] + r5[i][j + 1]),
                        min(d2[i][j] + l2[i][j - 1], d5[i][j] + l5[i][j - 1]),
                        min(d2[i][j] + r2[i][j + 1], d5[i][j] + r5[i][j + 1])
                    )
        return ret

    def maxTrailingZeros2(self, grid: List[List[int]]) -> int:
        import numpy as np
        A = np.array(grid)

        def cums(d):
            C = sum(A % d ** i == 0 for i in range(1, 10))
            return C.cumsum(0) + C.cumsum(1) - C

        return max(np.minimum(cums(2), cums(5)).max()
                   for _ in range(4)
                   if [A := np.rot90(A)])


so = Solution()
print(so.maxTrailingZeros(grid=[[23, 17, 15, 3, 20], [8, 1, 20, 27, 11], [9, 4, 6, 2, 21], [40, 9, 1, 10, 6], [22, 7, 4, 5, 3]]))
print(so.maxTrailingZeros([[1], [5], [2], [4], [25]]))
print(so.maxTrailingZeros([[899, 727, 165, 249, 531, 300, 542, 890], [981, 587, 565, 943, 875, 498, 582, 672], [106, 902, 524, 725, 699, 778, 365, 220]]))
