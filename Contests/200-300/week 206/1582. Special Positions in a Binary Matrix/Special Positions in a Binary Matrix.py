#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Special Positions in a Binary Matrix
@time: 2020/09/13 10:30
"""


class Solution:
    def numSpecial(self, mat: list(list())) -> int:
        m, n = len(mat), len(mat[0])
        ret = 0
        for i in range(m):
            col_one = -1
            cnt = 0
            for j in range(n):
                if mat[i][j] == 1:
                    cnt += 1
                    col_one = j
                    if cnt > 1:
                        break
            else:
                if col_one == -1: continue
                for k in range(m):
                    if k != i and mat[k][col_one] == 1:
                        break
                else:
                    ret += 1
        return ret


so = Solution()
print(so.numSpecial([[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]]))
