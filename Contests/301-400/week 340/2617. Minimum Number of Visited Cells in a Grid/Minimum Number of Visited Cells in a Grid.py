#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Visited Cells in a Grid.py 
@time: 2023/04/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque([[0, 0, 0]])
        visited = set([(0, 0)])
        while q:
            step, io, jo = q.popleft()
            if (io, jo) == (m - 1, n - 1):
                return step + 1
            maxj = grid[io][jo] + jo
            maxi = grid[io][jo] + io
            for k in range(jo + 1, min(maxj + 1, n)):
                if (io, k) not in visited:
                    q.append((step + 1, io, k))
                    if (io, k) == (m - 1, n - 1):
                        return step + 2
                    visited.add((io, k))
            for k in range(io + 1, min(maxi + 1, m)):
                if (k, jo) not in visited:
                    q.append((step + 1, k, jo))
                    if (k, jo) == (m - 1, n - 1):
                        return step + 2
                    visited.add((k, jo))
        return -1
