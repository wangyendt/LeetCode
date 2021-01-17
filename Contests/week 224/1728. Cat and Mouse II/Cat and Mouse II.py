#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Cat and Mouse II.py 
@time: 2021/01/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import functools


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        mouse_pos = cat_pos = None
        # Search the start pos of mouse and cat
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'M':
                    mouse_pos = (i, j)
                elif grid[i][j] == 'C':
                    cat_pos = (i, j)

        @functools.lru_cache(None)
        def dp(turn, mouse_pos, cat_pos):
            if turn == m * n * 2:
                # We already search the whole grid
                return False
            if turn % 2 == 0:
                # Mouse
                i, j = mouse_pos
                for di, dj in dirs:
                    for jump in range(mouseJump + 1):
                        # Note that we want to do range(mouseJump + 1) instead of range(1, mouseJump + 1)
                        # considering the case that we can stay at the same postion for next turn.
                        new_i, new_j = i + di * jump, j + dj * jump
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] != '#':
                            # Valid pos
                            if dp(turn + 1, (new_i, new_j), cat_pos) or grid[new_i][new_j] == 'F':
                                return True
                        else:
                            # Stop extending the jump since we cannot go further
                            break
                return False
            else:
                # Cat
                i, j = cat_pos
                for di, dj in dirs:
                    for jump in range(catJump + 1):
                        new_i, new_j = i + di * jump, j + dj * jump
                        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] != '#':
                            if not dp(turn + 1, mouse_pos, (new_i, new_j)) or (new_i, new_j) == mouse_pos or \
                                    grid[new_i][new_j] == 'F':
                                # This condition will also handle the case that the cat cannot jump through the mouse
                                return False
                        else:
                            break
                return True

        return dp(0, mouse_pos, cat_pos)
