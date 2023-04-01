#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Disconnect Path in a Binary Matrix by at Most One Flip.py 
@time: 2023/02/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == j == 0 or grid[i][j] == 0:
                    continue
                if (i == 0 or grid[i - 1][j] == 0) and (j == 0 and grid[i][j - 1] == 0):
                    grid[i][j] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i == m - 1 and j == n - 1) or grid[i][j] == 0:
                    continue
                if (i == m - 1 or grid[i + 1][j] == 0) and (j == n - 1 or grid[i][j + 1] == 0):
                    grid[i][j] = 0
        count = collections.Counter(i + j for i in range(m) for j in range(n) if grid[i][j])
        return any(count[i] < 2 for i in range(1, n + m - 2))
