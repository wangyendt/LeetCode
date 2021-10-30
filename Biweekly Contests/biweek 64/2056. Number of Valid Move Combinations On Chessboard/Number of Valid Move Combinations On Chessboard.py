#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Valid Move Combinations On Chessboard.py 
@time: 2021/10/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        N = len(pieces)

        qdirections = [(1, 1), (-1, 1), (0, 1), (-1, -1), (1, -1), (0, -1), (1, 0), (-1, 0)]
        bdirections = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        rdirections = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        possible = []
        for piece in pieces:
            if piece == "rook":
                possible.append(rdirections)
            elif piece == "queen":
                possible.append(qdirections)
            else:
                possible.append(bdirections)

        moves = 0

        def go(index):
            if index == N:
                # print(pieces[0], possible[0][dirs[0]], spaces[0])
                # simulate
                valid = True

                current = []
                for x, y in positions:
                    current.append((x, y))

                t = 0
                moved = True
                while moved:
                    moved = False

                    for i in range(N):
                        if spaces[i] > t:
                            current[i] = (
                                current[i][0] + possible[i][dirs[i]][0], current[i][1] + possible[i][dirs[i]][1])
                            moved = True

                    t += 1
                    s = set()
                    for i in range(N):
                        if current[i] in s:
                            valid = False
                            break
                        s.add(current[i])

                if valid:
                    nonlocal moves
                    moves += 1
                return

            dirs[index] = 0
            spaces[index] = 0
            go(index + 1)

            for i in range(len(possible[index])):
                dx, dy = possible[index][i][0], possible[index][i][1]
                dirs[index] = i

                nx, ny = positions[index][0] + dx, positions[index][1] + dy
                spaces[index] = 1

                while 1 <= nx <= 8 and 1 <= ny <= 8:
                    go(index + 1)
                    spaces[index] += 1
                    nx, ny = nx + dx, ny + dy

        dirs = [0] * N
        spaces = [0] * N
        go(0)
        return moves
