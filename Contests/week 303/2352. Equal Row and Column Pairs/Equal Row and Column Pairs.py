#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Equal Row and Column Pairs.py 
@time: 2022/07/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        g2 = list(map(list, zip(*grid)))
        ret = 0
        for i in range(n):
            for j in range(n):
                if grid[i] == g2[j]:
                    ret += 1
        return ret


so = Solution()
print(so.equalPairs(grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
