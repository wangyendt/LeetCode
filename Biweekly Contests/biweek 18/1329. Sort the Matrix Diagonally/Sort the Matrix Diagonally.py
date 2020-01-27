#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Sort the Matrix Diagonally
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/27 16:00
@Desc   ：
=================================================="""


class Solution:
    def diagonalSort(self, mat: list(list())) -> list(list()):
        m, n = len(mat), len(mat[0])
        seen = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not seen[i][j]:
                    s_i, s_j = i, j
                    res = []
                    while s_i < m and s_j < n:
                        res.append(mat[s_i][s_j])
                        seen[s_i][s_j] = 1
                        s_i += 1
                        s_j += 1
                    res.sort()
                    t_i, t_j = i, j
                    cnt = 0
                    while t_i < m and t_j < n:
                        mat[t_i][t_j] = res[cnt]
                        t_i += 1
                        t_j += 1
                        cnt += 1
        return mat


so = Solution()
print(so.diagonalSort(mat=[[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))
