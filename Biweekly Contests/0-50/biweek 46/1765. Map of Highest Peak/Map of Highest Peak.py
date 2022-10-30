#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Map of Highest Peak.py 
@time: 2021/02/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        water = []
        seen = set()
        m, n = len(isWater), len(isWater[0])
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    water.append((i, j))
                    seen.add((i, j))
        ret = [[0 for _ in range(n)] for _ in range(m)]
        height = 0
        while water:
            new = []
            for w in water:
                ret[w[0]][w[1]] = height
                for ii, jj in [(w[0] - 1, w[1]), (w[0] + 1, w[1]), (w[0], w[1] - 1), (w[0], w[1] + 1)]:
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen:
                        new.append((ii, jj))
                        seen.add((ii, jj))
            water = new
            height += 1
        return ret


so = Solution()
print(so.highestPeak(isWater=[[0, 1], [0, 0]]))
