# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/6 17:40
# software: PyCharm

class Solution:
    def solve(self, board: list(list())) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        mask = [[0 for _ in range(n)] for _ in range(m)]

        def cool(i, j, m, n):
            return 0 <= i <= m - 1 and 0 <= j <= n - 1

        for i in range(m):
            mask[i][0] = 1
            mask[i][-1] = 1
        for j in range(n):
            mask[0][j] = 1
            mask[-1][j] = 1
        for i in range(m):
            stack = [(i, 0), (i, n - 1)]
            while stack:
                ii, jj = stack.pop()
                if board[ii][jj] == 'O':
                    mask[ii][jj] = 1
                    up = (ii - 1, jj)
                    left = (ii, jj - 1)
                    down = (ii + 1, jj)
                    right = (ii, jj + 1)
                    for d in [up, left, down, right]:
                        if cool(d[0], d[1], m, n) and mask[d[0]][d[1]] == 0:
                            stack.append((d[0], d[1]))
        for j in range(n):
            stack = [(0, j), (m - 1, j)]
            while stack:
                ii, jj = stack.pop()
                if board[ii][jj] == 'O':
                    mask[ii][jj] = 1
                    up = (ii - 1, jj)
                    left = (ii, jj - 1)
                    down = (ii + 1, jj)
                    right = (ii, jj + 1)
                    for d in [up, left, down, right]:
                        if cool(d[0], d[1], m, n) and mask[d[0]][d[1]] == 0:
                            stack.append((d[0], d[1]))
        for i in range(m):
            for j in range(n):
                if mask[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'


so = Solution()
l = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
l = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"], ["X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"],
     ["X", "X", "O", "X", "O"]]
[print(ll) for ll in l]
print('------------------')
so.solve(l)
print('------------------')
[print(ll) for ll in l]
print('------------------')
lres = [["O", "X", "X", "O", "X"], ["X", "X", "X", "X", "O"], ["X", "X", "X", "O", "X"], ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]]
[print(ll) for ll in lres]
