#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Cells with Odd Values in a Matrix
@time: 2019/11/10 21:18
"""


class Solution:
    def oddCells(self, n: int, m: int, indices: list(list())) -> int:
        A = [[0 for _ in range(m)] for _ in range(n)]
        for r, c in indices:
            for i in range(m):
                A[r][i] += 1
            for i in range(n):
                A[i][c] += 1
        ret = 0
        for r in range(n):
            for c in range(m):
                if A[r][c] % 2 == 1:
                    ret += 1
        return ret


so = Solution()
print(so.oddCells(n=2, m=3, indices=[[0, 1], [1, 1]]))
