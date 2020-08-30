#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Minimum Number of Days to Disconnect Island.py 
@time: 2020/08/31
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def minDays(self, grid: list(list())) -> int:
        n = len(grid)
        m = len(grid[0])

        def count(grid):
            vis = [[False] * m for i in range(n)]

            def isValid(i, j):
                if i < 0 or i >= n or j < 0 or j >= m or vis[i][j] or not grid[i][j]:
                    return False
                return True

            def dfs(i, j):
                if isValid(i, j):
                    vis[i][j] = True
                    dfs(i + 1, j)
                    dfs(i - 1, j)
                    dfs(i, j + 1)
                    dfs(i, j - 1)

            cnt = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] and not vis[i][j]:
                        cnt += 1
                        dfs(i, j)

            return cnt

        islands = count(grid)
        if islands != 1:
            return 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    grid[i][j] = 0
                    islands = count(grid)
                    if islands != 1:
                        return 1
                    grid[i][j] = 1
        return 2
