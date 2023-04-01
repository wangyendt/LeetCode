#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/15 15:56
@Author:  wang121ye
@File: Lucky Numbers in a Matrix.py
@Software: PyCharm
"""


class Solution:
    def luckyNumbers(self, matrix: list(list())) -> list:
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for i in range(m):
            k, min_ = (i, 0), matrix[i][0]
            for j in range(1, n):
                if matrix[i][j] < min_:
                    min_ = matrix[i][j]
                    k = (i, j)
            rows.add(k)
        for j in range(n):
            k, max_ = (0, j), matrix[0][j]
            for i in range(1, m):
                if matrix[i][j] > max_:
                    max_ = matrix[i][j]
                    k = (i, j)
            cols.add(k)
        res = rows & cols
        # print(res)
        return [matrix[r[0]][r[1]] for r in res]


so = Solution()
print(so.luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(so.luckyNumbers(matrix=[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
print(so.luckyNumbers(matrix=[[7, 8], [1, 2]]))
