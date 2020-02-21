#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> The K Weakest Rows in a Matrix
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/2/21 18:16
@Desc   ：
=================================================="""

import functools


class Solution:
    def kWeakestRows(self, mat: list(list()), k: int) -> list:
        def compare(i, j):
            si, sj = sum(mat[i]), sum(mat[j])
            if si > sj:
                return 1
            elif si == sj:
                return 0
            else:
                return -1

        return sorted(list(range(len(mat))), key=functools.cmp_to_key(compare))[:k]


so = Solution()
print(so.kWeakestRows(mat=
                      [[1, 1, 0, 0, 0],
                       [1, 1, 1, 1, 0],
                       [1, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0],
                       [1, 1, 1, 1, 1]],
                      k=3))
print(so.kWeakestRows(mat=
                      [[1, 0, 0, 0],
                       [1, 1, 1, 1],
                       [1, 0, 0, 0],
                       [1, 0, 0, 0]],
                      k=2))
