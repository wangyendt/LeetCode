#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
@time: 2019/12/9 16:15
"""


class Solution:
    def minFlips(self, mat: list(list())) -> int:
        m, n = len(mat), len(mat[0])

        def flip(M, i, j):
            boundary_handle = lambda c: (min(max(c[0], 0), m - 1), min(max(c[1], 0), n - 1))
            todo = set(map(boundary_handle, {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i, j)}))
            for tdx, tdy in todo:
                M[tdx][tdy] = 1 - M[tdx][tdy]

        def success(M):
            return sum(map(sum, M)) == 0

        ret = m * n
        b_success = False
        for k in range(1 << (m * n)):
            M_ = [[mat[ii][jj] for jj in range(n)] for ii in range(m)]
            cnt = 0
            for i in range(m):
                for j in range(n):
                    t = i * n + j
                    will_flip = (k >> t) & 1
                    if will_flip:
                        flip(M_, i, j)
                        cnt += 1
            if success(M_):
                ret = min(ret, cnt)
                b_success = True

        return ret if b_success else -1


so = Solution()
print(so.minFlips(mat=[[0, 0], [0, 1]]))
print(so.minFlips(mat=[[0]]))
print(so.minFlips(mat=[[1, 1, 1], [1, 0, 1], [0, 0, 0]]))
print(so.minFlips(mat=[[1, 0, 0], [1, 0, 0]]))
