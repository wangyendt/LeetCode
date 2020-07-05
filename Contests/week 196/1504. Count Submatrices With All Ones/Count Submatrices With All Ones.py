#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count Submatrices With All Ones
@time: 2020/07/05 10:38
"""


class Solution:
    def numSubmat(self, mat: list(list())) -> int:
        m, n = len(mat), len(mat[0])

        def find_prefix_count(p_arr, arr):
            for i in range(0, m):
                for j in range(n - 1, -1, -1):
                    if not arr[i][j]:
                        continue
                    if j != n - 1:
                        p_arr[i][j] += p_arr[i][j + 1]
                    p_arr[i][j] += arr[i][j]

        p_mat = [[0 for _ in range(n)] for _ in range(m)]
        find_prefix_count(p_mat, mat)
        ret = 0
        for j in range(0, n):
            i = n - 1
            q = []
            to_sum = 0
            while i >= 0:
                c = 0
                while len(q) != 0 and q[-1][0] > p_mat[i][j]:
                    to_sum -= (q[-1][1] + 1) * (q[-1][0] - p_mat[i][j])
                    c += q[-1][1] + 1
                    q.pop()
                to_sum += p_mat[i][j]
                ret += to_sum
                q.append((p_mat[i][j], c))
                i -= 1
        return ret
