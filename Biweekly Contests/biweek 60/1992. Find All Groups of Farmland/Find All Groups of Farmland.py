#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find All Groups of Farmland.py 
@time: 2021/09/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        seen = [[False for _ in range(n)] for _ in range(m)]

        def find(i, j):
            i_, j_ = i, j
            while i < m:
                if land[i][j_] == 0:
                    break
                i += 1
            while j < n:
                if land[i_][j] == 0:
                    break
                j += 1
            for ii in range(i_, i):
                for jj in range(j_, j):
                    seen[ii][jj] = True
            return (i_, j_, i - 1, j - 1)

        ret = []
        for i in range(m):
            for j in range(n):
                if not seen[i][j]:
                    if land[i][j] == 1:
                        ret.append(find(i, j))
                seen[i][j] = True
        return ret
