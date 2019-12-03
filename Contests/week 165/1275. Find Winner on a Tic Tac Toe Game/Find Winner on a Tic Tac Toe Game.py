#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find Winner on a Tic Tac Toe Game
@time: 2019/12/2 16:10
"""


class Solution:
    def tictactoe(self, moves: list(list())) -> str:
        def win(arr):
            return any([all([co in arr for co in comb]) for comb in [
                (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)
            ]])

        sub2ind = lambda x: x[0] * 3 + x[1] + 1
        w1 = win(list(map(sub2ind, moves[::2])))
        w2 = win(list(map(sub2ind, moves[1::2])))
        if w1: return 'A'
        if w2: return 'B'
        if len(moves) == 9: return 'Draw'
        return 'Pending'


so = Solution()
print(so.tictactoe(moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
print(so.tictactoe(moves=[[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))
print(so.tictactoe(moves=[[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))
print(so.tictactoe(moves=[[0, 0], [1, 1]]))
