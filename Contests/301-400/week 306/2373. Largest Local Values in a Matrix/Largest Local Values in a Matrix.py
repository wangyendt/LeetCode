#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Largest Local Values in a Matrix.py 
@time: 2022/10/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import itertools


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ret = [[0 for _ in range(n - 2)] for _ in range(m - 2)]
        for i, j in itertools.product(range(m), range(n)):
            if 0 < i < m - 1 and 0 < j < n - 1:
                ret[i - 1][j - 1] = max(max(grid[i - 1][j - 1:j + 2]), max(grid[i][j - 1:j + 2]), max(grid[i + 1][j - 1:j + 2]))
        return ret
