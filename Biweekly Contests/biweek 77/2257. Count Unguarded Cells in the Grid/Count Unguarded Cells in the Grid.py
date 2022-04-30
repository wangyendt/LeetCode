#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Unguarded Cells in the Grid.py 
@time: 2022/04/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for gr, gc in guards:
            grid[gr][gc] = 1
        for wr, wc in walls:
            grid[wr][wc] = 2
        # up = [-1] * n
        can_see_grid = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            can_see = False
            for i in range(m):
                if grid[i][j] == 1:
                    can_see = True
                elif grid[i][j] == 2:
                    can_see = False
                if can_see:
                    can_see_grid[i][j] = 1
        for j in range(n):
            can_see = False
            for i in range(m)[::-1]:
                if grid[i][j] == 1:
                    can_see = True
                elif grid[i][j] == 2:
                    can_see = False
                if can_see:
                    can_see_grid[i][j] = 1
        # left = [-1] * m
        for i in range(m):
            can_see = False
            for j in range(n):
                if grid[i][j] == 1:
                    can_see = True
                elif grid[i][j] == 2:
                    can_see = False
                if can_see:
                    can_see_grid[i][j] = 1
        for i in range(m):
            can_see = False
            for j in range(n)[::-1]:
                if grid[i][j] == 1:
                    can_see = True
                elif grid[i][j] == 2:
                    can_see = False
                if can_see:
                    can_see_grid[i][j] = 1

        ret = 0
        # print(up)
        # print(left)
        # [print(c) for c in can_see_grid]
        for i in range(m):
            for j in range(n):
                if can_see_grid[i][j] == 0 and grid[i][j] == 0:
                    ret += 1
        return ret


so = Solution()
# print(so.countUnguarded(m=4, n=6, guards=[[0, 0], [1, 1], [2, 3]], walls=[[0, 1], [2, 2], [1, 4]]))
print(so.countUnguarded(7, 1, [[0, 0], [4, 0], [1, 0]], [[6, 0], [5, 0], [3, 0]]))
print(so.countUnguarded(40,
                        37,
                        [[25, 34], [14, 34], [12, 17], [8, 1], [5, 34], [33, 17], [3, 8], [28, 35], [11, 16], [1, 10],
                         [3, 24], [17, 2], [9, 17], [28, 10], [22, 30], [30, 4], [14, 5], [32, 9], [4, 6], [24, 8],
                         [4, 31], [7, 11], [31, 2], [29, 2], [33, 10], [1, 15], [20, 6], [15, 26], [29, 26], [1, 14],
                         [6, 32], [31, 13], [6, 18], [19, 11], [31, 12], [7, 34], [17, 28], [12, 12], [21, 27],
                         [19, 33], [8, 4], [36, 13], [2, 30], [38, 23], [35, 9], [37, 21], [31, 9], [31, 10], [30, 11],
                         [30, 19], [32, 35], [11, 31], [34, 9], [39, 5], [6, 1], [24, 21], [2, 24], [10, 22], [14, 36],
                         [0, 35], [25, 26], [26, 9]],
                        [[11, 25], [29, 14], [37, 5], [13, 27], [4, 28], [37, 33], [31, 1], [15, 7], [10, 24], [9, 4],
                         [36, 15], [29, 4], [12, 33], [0, 23], [32, 19], [19, 32], [38, 3], [26, 10]]))
