#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Dice Roll Simulation.py 
@time: 2019/10/13
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

from functools import lru_cache


class Solution:
    def dieSimulator(self, n, rollMax):
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(i, j, k):
            # i rolls, recently rolled j, k times
            if i == 0:
                return 1
            ans = 0
            for d in range(6):
                if d != j:
                    ans += dp(i - 1, d, 1)
                elif k + 1 <= rollMax[d]:
                    ans += dp(i - 1, d, k + 1)
            ans %= MOD
            return ans

        return dp(n, -1, 0) % MOD
