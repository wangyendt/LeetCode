# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Maximum Number of Points with Cost.py
@time: 2021/07/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *


class Solution:
    def maxPoints(self, P: List[List[int]]) -> int:
        m, n = len(P), len(P[0])
        if m == 1: return max(P[0])
        if n == 1: return sum(sum(x) for x in P)

        def left(arr):
            lft = [arr[0]] + [0] * (n - 1)
            for i in range(1, n): lft[i] = max(lft[i - 1] - 1, arr[i])
            return lft

        def right(arr):
            rgt = [0] * (n - 1) + [arr[-1]]
            for i in range(n - 2, -1, -1): rgt[i] = max(rgt[i + 1] - 1, arr[i])
            return rgt

        pre = P[0]
        for i in range(m - 1):
            lft, rgt, cur = left(pre), right(pre), [0] * n
            for j in range(n):
                cur[j] = P[i + 1][j] + max(lft[j], rgt[j])
            pre = cur[:]

        return max(pre)
