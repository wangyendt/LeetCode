#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Stone Game V.py 
@time: 2020/08/24
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import functools


class Solution:
    def stoneGameV(self, A):
        n = len(A)
        prefix = [0] * (n + 1)
        for i, a in enumerate(A):
            prefix[i + 1] = prefix[i] + A[i]

        @functools.lru_cache(None)
        def dp(i, j):
            if i == j: return 0
            res = 0
            for m in range(i, j):
                left = prefix[m + 1] - prefix[i]
                right = prefix[j + 1] - prefix[m + 1]
                if left <= right:
                    res = max(res, dp(i, m) + left)
                if left >= right:
                    res = max(res, dp(m + 1, j) + right)
            return res

        return dp(0, n - 1)
