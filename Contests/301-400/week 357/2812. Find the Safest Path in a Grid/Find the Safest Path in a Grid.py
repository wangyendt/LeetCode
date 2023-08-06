#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find the Safest Path in a Grid.py 
@time: 2023/08/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        adj_list = collections.defaultdict(list)
        board = [[float("inf")] * nc for _ in range(nr)]
        q = collections.deque([])
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    q.append((r, c, 0))

        visited = set()
        while q:
            for _ in range(len(q)):
                r, c, dist = q.popleft()
                if r < 0 or r >= nr or c < 0 or c >= nc:
                    continue
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                board[r][c] = min(board[r][c], dist)

                for r_inc, c_inc in directions:
                    r_next, c_next = r + r_inc, c + c_inc
                    q.append((r_next, c_next, dist + 1))

        output = float("inf")
        visited = set()
        heap = [(-board[0][0], 0, 0)]

        while heap:
            d, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            output = min(output, -1 * d)
            if r == nr - 1 and c == nc - 1:
                return output

            visited.add((r, c))
            for r_inc, c_inc in directions:
                r_next, c_next = r + r_inc, c + c_inc
                if r_next < 0 or r_next >= nr or c_next < 0 or c_next >= nc:
                    continue
                heapq.heappush(heap, (-board[r_next][c_next], r_next, c_next))


so = Solution()
print(so.maximumSafenessFactor(grid=[[0, 0, 1], [0, 0, 0], [0, 0, 0]]))
