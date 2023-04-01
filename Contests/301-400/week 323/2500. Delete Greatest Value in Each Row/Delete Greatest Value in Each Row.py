#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Delete Greatest Value in Each Row.py 
@time: 2022/12/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i, g in enumerate(grid):
            grid[i] = list(sorted(g))
        ret = 0
        for j in range(len(grid[0])):
            ret += max(grid[i][j] for i in range(len(grid)))
        return ret


so = Solution()
print(so.deleteGreatestValue(grid=[[1, 2, 4], [3, 3, 1]]))
