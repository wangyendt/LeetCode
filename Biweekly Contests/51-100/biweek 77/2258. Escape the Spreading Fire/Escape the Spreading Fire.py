#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Escape the Spreading Fire.py 
@time: 2022/04/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *

from heapq import heappush, heappop, heapify


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ESCAPER, FIRE, WALL = 1, 0, 2
        fires = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fires.append((i, j))

        def check(start):
            visited = set()
            heap = [(start, ESCAPER, 0, 0)]
            first_reach = float('inf')
            for i, j in fires:
                heap.append((0, FIRE, i, j))
            heapify(heap)
            while heap:
                d, t, r, c = heappop(heap)
                if t == ESCAPER and (r, c) == (m - 1, n - 1) and (first_reach == float('inf') or first_reach == d):
                    return True
                if (r, c) in visited: continue
                if (r, c) == (m - 1, n - 1):
                    first_reach = min(first_reach, d)
                visited.add((r, c))
                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    if (0 <= r + dr < m) and (0 <= c + dc < n) and grid[r + dr][c + dc] != WALL:
                        heappush(heap, (d + 1, t, r + dr, c + dc))
            return False

        left, right = -1, m * n - 1
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        if left == m * n - 1:
            return 10 ** 9
        return left
