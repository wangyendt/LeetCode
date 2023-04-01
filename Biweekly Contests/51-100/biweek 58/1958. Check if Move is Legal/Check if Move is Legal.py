#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if Move is Legal.py 
@time: 2021/08/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        m, n = len(board), len(board[0])
        stack = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for sr, sc in stack:
            r, c = rMove, cMove
            state = 0
            while True:
                r += sr
                c += sc
                if 0 <= r < m and 0 <= c < n:
                    if board[r][c] in 'WB':
                        if board[r][c] != color:
                            state = 1
                        else:
                            if state == 0:
                                break
                            if state == 1 and board[r][c] == color:
                                return True
                    else:
                        break
                else:
                    break
        return False


so = Solution()
print(so.checkMove(
    [["B", "B", ".", ".", "B", "W", "W", "."],
     [".", "W", "W", ".", "B", "W", "B", "B"],
     [".", "W", "B", "B", "W", ".", "W", "."],
     ["B", ".", ".", "B", "W", "W", "W", "."],
     ["W", "W", "W", "B", "W", ".", "B", "W"],
     [".", ".", ".", "W", ".", "W", ".", "B"],
     ["B", "B", "W", "B", "B", "W", "W", "B"],
     ["W", ".", "W", "W", ".", "B", ".", "W"]],
    2,
    5,
    "W"))
