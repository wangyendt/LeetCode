#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Longest Increasing Path in a Matrix
@time: 2020/06/25 03:07
"""


class Solution:
    def longestIncreasingPath(self, matrix: list(list())) -> int:
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def explore(r: int, c: int) -> int:
            cur = 1
            is_end = True
            if not dp[r][c]:
                for ud, lr in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
                    nr, nc = r + ud, c + lr
                    if 0 <= nr < m and 0 <= nc < n and matrix[r][c] < matrix[nr][nc]:
                        cur = max(cur, explore(nr, nc) + 1)
                        is_end = False
                if is_end:
                    dp[r][c] = 1
                else:
                    dp[r][c] = cur
            return dp[r][c]

        for i in range(m):
            for j in range(n):
                if not dp[i][j]:
                    explore(i, j)
                dp[i][j] = max(1, dp[i][j])
        ret = 0
        for i in range(m):
            for j in range(n):
                ret = max(ret, dp[i][j])
        return ret


so = Solution()
print(so.longestIncreasingPath(matrix=[
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]))
print(so.longestIncreasingPath(matrix=[
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]))
print(so.longestIncreasingPath([[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]))