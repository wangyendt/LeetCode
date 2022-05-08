#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if There Is a Valid Parentheses String Path.py 
@time: 2022/05/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (n + m) % 2 == 0: return False
        dp = [[set() for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                d = 1 if grid[i][j] == '(' else -1
                for a in dp[i - 1][j] if i else []:
                    if a + d >= 0:
                        dp[i][j].add(a + d)
                for a in dp[i][j - 1] if j else []:
                    if a + d >= 0:
                        dp[i][j].add(a + d)
                if i == 0 and j == 0:
                    if d >= 0:
                        dp[i][j].add(d)
        return 0 in dp[-1][-1]
