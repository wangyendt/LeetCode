#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Matrix Block Sum
@time: 2020/1/15 14:28
"""

import itertools


class Solution:
    def matrixBlockSum(self, A, K):
        m, n = len(A), len(A[0])
        ps = [*zip(*map(itertools.accumulate, zip(*map(itertools.accumulate, A))))]

        def s(i, j):
            return i >= 0 <= j and ps[min(i, m - 1)][min(j, n - 1)]

        return [[s(i + K, j + K) - s(i - K - 1, j + K) - s(i + K, j - K - 1) + s(i - K - 1, j - K - 1)
                 for j in range(n)] for i in range(m)]


so = Solution()
print(so.matrixBlockSum(A=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=1))
print(so.matrixBlockSum(A=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=2))
