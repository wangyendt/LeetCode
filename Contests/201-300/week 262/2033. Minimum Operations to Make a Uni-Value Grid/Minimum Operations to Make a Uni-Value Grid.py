#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Operations to Make a Uni-Value Grid.py
@time: 2021/10/10
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        A = [grid[i][j] for i in range(m) for j in range(n)]
        A.sort()
        l = len(A)
        target = A[l // 2]
        ret = 0
        for a in A:
            if (target - a) % x != 0:
                return -1
            ret += abs(target - a) // x
        return ret
