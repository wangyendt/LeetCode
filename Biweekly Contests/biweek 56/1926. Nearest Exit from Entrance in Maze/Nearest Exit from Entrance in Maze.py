# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Nearest Exit from Entrance in Maze.py
@time: 2021/07/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x, y = entrance
        m, n, infi = len(maze), len(maze[0]), int(1e5)
        reached = lambda p, q: (not p == x or not q == y) and (p == 0 or q == 0 or p == m - 1 or q == n - 1)
        q, ans = collections.deque(), 0
        q.append((x, y, ans))
        directions = [1, 0, -1, 0, 1]
        while q:
            row, col, ans = q.popleft()
            for i in range(4):
                r, c = row + directions[i], col + directions[i + 1]
                if r < 0 or c < 0 or r == m or c == n or maze[r][c] == '+':
                    continue
                if reached(r, c):
                    return ans + 1
                maze[r][c] = '+'
                q.append((r, c, ans + 1))
        return -1
