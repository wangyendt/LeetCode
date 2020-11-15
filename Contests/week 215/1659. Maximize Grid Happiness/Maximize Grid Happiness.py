#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximize Grid Happiness.py 
@time: 2020/11/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import functools


class Solution:
    def getMaxGridHappiness(self, m, n, I, E):
        InG, ExG, InL, ExL = 120, 40, -30, 20
        fine = [[0, 0, 0], [0, 2 * InL, InL + ExL], [0, InL + ExL, 2 * ExL]]

        @functools.lru_cache(None)
        def dp(index, row, I, E):
            if index == -1: return 0

            R, C, ans = index // n, index % n, []
            neibs = [(1, I - 1, E, InG), (2, I, E - 1, ExG), (0, I, E, 0)]

            for val, dx, dy, gain in neibs:
                tmp = 0
                if dx >= 0 and dy >= 0:
                    tmp = dp(index - 1, (val,) + row[:-1], dx, dy) + gain
                    if C < n - 1: tmp += fine[val][row[0]]  # right neighbor
                    if R < m - 1: tmp += fine[val][row[-1]]  # down neighbor
                ans.append(tmp)

            return max(ans)

        if m < n: m, n = n, m

        return dp(m * n - 1, tuple([0] * n), I, E)
