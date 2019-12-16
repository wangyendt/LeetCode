#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Side Length of a Square with Sum Less than or Equal to Threshold
@time: 2019/12/16 17:42
"""

import itertools


class Solution:
    def maxSideLength(self, G: list(list()), t: int) -> int:
        M, N, m = len(G), len(G[0]), 0;
        S = [[0] * (N + 1) for _ in range(M + 1)]
        S[1] = list(itertools.accumulate([0] + G[0]))
        for i in range(1, M):
            s = list(itertools.accumulate(G[i]))
            for j in range(N): S[i + 1][j + 1] = s[j] + S[i][j + 1]
        for i, j in itertools.product(range(M), range(N)):
            for L in range(m + 1, min(M - i + 1, N - j + 1)):
                if S[i + L][j + L] - S[i][j + L] - S[i + L][j] + S[i][j] <= t:
                    m = max(m, L)
                else:
                    break
        return m
