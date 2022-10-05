#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Sum of an Hourglass.py 
@time: 2022/10/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import itertools


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = 0
        for i, j in itertools.product(range(m), range(n)):
            if i + 3 <= m and j + 3 <= n:
                res = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                ret = max(ret, res)
        return ret


so = Solution()
print(so.maxSum(grid=[[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]))
