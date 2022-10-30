#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Detect Cycles in 2D Grid.py 
@time: 2020/08/22
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def containsCycle(self, grid: list(list())) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        cycle = False

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def is_cycle(x, y, px, py):
            visited[x][y] = True
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + di, y + dj
                if is_valid(nx, ny) and grid[nx][ny] == grid[x][y] and not (px == nx and py == ny):
                    if visited[nx][ny]:
                        return True
                    else:
                        check = is_cycle(nx, ny, x, y)
                        if check: return True
            return False

        for i in range(m):
            if cycle: break
            for j in range(n):
                if not visited[i][j]:
                    cycle = is_cycle(i, j, -1, -1)
                if cycle: break
        return cycle


so = Solution()
print(so.containsCycle(grid=[["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]))
