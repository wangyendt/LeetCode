#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if Matrix Is X-Matrix.py 
@time: 2022/06/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import itertools


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i, j in itertools.product(range(n), range(n)):
            if i == j or i + j == n - 1:
                if grid[i][j] == 0: return False
            else:
                if grid[i][j] != 0: return False
        return True
