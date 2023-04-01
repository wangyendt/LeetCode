#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Ways to Stay in the Same Place After Some Steps
@time: 2019/11/27 16:23
"""


class Solution:
    def numWays(self, steps, n, mod=10 ** 9 + 7):
        A = [0, 1]
        for t in range(steps):
            A[1:] = [sum(A[i - 1:i + 2]) % mod for i in range(1, min(n + 1, t + 3))]
        return A[1] % mod
