#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Largest 1-Bordered Square.py 
@time: 2019/07/28
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def largest1BorderedSquare(self, A: list(list())) -> int:
        m, n = len(A), len(A[0])
        res = 0
        top, left = [a[:] for a in A], [a[:] for a in A]
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    if i: top[i][j] = top[i - 1][j] + 1
                    if j: left[i][j] = left[i][j - 1] + 1
        for r in range(min(m, n), 0, -1):
            for i in range(m - r + 1):
                for j in range(n - r + 1):
                    if min(top[i + r - 1][j], top[i + r - 1][j + r - 1], left[i]
                    [j + r - 1], left[i + r - 1][j + r - 1]) >= r:
                        return r * r
        return 0


so = Solution()
print(so.largest1BorderedSquare([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
