#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Get Maximum in Generated Array
@time: 2020/11/08 10:32
"""

import functools


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        @functools.lru_cache(None)
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i % 2 == 0:
                return dp(i // 2)
            if i % 2 == 1:
                return dp(i // 2) + dp(i // 2 + 1)

        return max([dp(i) for i in range(n + 1)])
