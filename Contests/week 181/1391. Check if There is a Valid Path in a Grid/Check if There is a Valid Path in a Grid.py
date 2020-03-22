#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/23 2:13
@Author:  wang121ye
@File: Check if There is a Valid Path in a Grid.py
@Software: PyCharm
"""


class Solution:
    def hasValidPath(self, A):
        m, n = len(A), len(A[0])
        uf = {(i, j): (i, j) for i in range(-1, m * 2 + 1) for j in range(-1, n * 2 + 1)}

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def merge(i, j, di, dj):
            uf[find((i, j))] = find((i + di, j + dj))

        for i in range(m):
            for j in range(n):
                if A[i][j] in [2, 5, 6]: merge(i * 2, j * 2, -1, 0)
                if A[i][j] in [1, 3, 5]: merge(i * 2, j * 2, 0, -1)
                if A[i][j] in [2, 3, 4]: merge(i * 2, j * 2, 1, 0)
                if A[i][j] in [1, 4, 6]: merge(i * 2, j * 2, 0, 1)
        return find((0, 0)) == find((m * 2 - 2, n * 2 - 2))