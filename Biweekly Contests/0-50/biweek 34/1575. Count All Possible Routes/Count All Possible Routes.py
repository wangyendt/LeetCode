#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Count All Possible Routes.py 
@time: 2020/09/05
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import functools

import collections


class Solution:
    def countRoutes(self, A: list, start: int, finish: int, fuel: int) -> int:
        n = len(A)
        MOD = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dp(i, k):
            if k < 0:
                return 0
            ans = 1 if i == finish else 0
            for j in range(n):
                if i == j:
                    continue
                ans += dp(j, k - abs(A[i] - A[j]))
            return ans % MOD

        return dp(start, fuel)


so = Solution()
# print(so.countRoutes(A=[2, 3, 6, 8, 4], start=1, finish=3, fuel=5))
print(so.countRoutes(A=[4, 3, 1], start=1, finish=0, fuel=6))
