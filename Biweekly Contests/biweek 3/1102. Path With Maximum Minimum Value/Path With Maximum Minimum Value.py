#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Path With Maximum Minimum Value.py 
@time: 2019/06/30
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""
import sys
import bisect


class Solution:
    def maximumMinimumPath(self, A: list(list())) -> int:
        visited = set()
        R, C = len(A), len(A[0])
        value = [[-sys.maxsize for _ in range(C)] for _ in range(R)]
        value[0][0] = A[0][0]

        def helper(i, j, r, c):
            return list(set([(min(max(i + p, 0), r - 1), min(max(j + q, 0), c - 1))
                             for p in [-1, 0, 1] for q in [-1, 0, 1]]) - {(i, j)})

        priorityQueue = [(0, 0, 0)]
        while True:
            cv, cx, cy = priorityQueue.pop()
            for (nx, ny) in helper(cx, cy, R, C):
                if min(value[cx][cy], A[nx][ny]) >= value[nx][ny] and not (nx, ny) in visited:
                    value[nx][ny] = min(value[cx][cy], A[nx][ny])
                    bisect.insort(priorityQueue, (value[nx][ny], nx, ny))
            if priorityQueue:
                visited.add(tuple(priorityQueue[-1][1:]))
            else:
                break
        return value[-1][-1] if value[-1][-1] != sys.maxsize else -1


so = Solution()
print(so.maximumMinimumPath([[5, 4, 5], [1, 2, 6], [7, 4, 6]]))
print(so.maximumMinimumPath([[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]))
print(so.maximumMinimumPath(
    [[3, 4, 6, 3, 4],
     [0, 2, 1, 1, 7],
     [8, 8, 3, 2, 7],
     [3, 2, 4, 9, 8],
     [4, 1, 2, 0, 0],
     [4, 6, 5, 4, 3]]))
