# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/24 10:30
# software: PyCharm

import bisect
import sys


class Solution:
    def shortestPathBinaryMatrix(self, grid: list(list())) -> int:
        [print(g) for g in grid]
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid)
        visited = set()
        value = [[sys.maxsize for _ in range(n)] for _ in range(n)]
        value[0][0] = 1

        def helper(i, j):
            return list(
                set([(min(max(i + p, 0), n - 1), min(max(j + q, 0), n - 1))
                     for p in [-1, 0, 1] for q in [-1, 0, 1]]) - {(i, j)})

        priorityQueue = [(0, 0, 0)]
        while True:
            print(priorityQueue)
            cv, cx, cy = priorityQueue.pop(0)
            for (nx, ny) in helper(cx, cy):
                # print(cv, nx, ny)
                if grid[nx][ny] == 0 and value[cx][cy] + 1 < value[nx][ny] and not (nx, ny) in visited:
                    bisect.insort(priorityQueue, (cv + 1, nx, ny))
                    value[nx][ny] = value[cx][cy] + 1
            # print(priorityQueue)
            if priorityQueue:
                visited.add(priorityQueue[0])
            else:
                break
        # print(visited, priorityQueue, value)
        return value[-1][-1] if value[-1][-1] != sys.maxsize else -1


so = Solution()
print(so.shortestPathBinaryMatrix([[0, 1], [1, 0]]), 2)
print(so.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]), 4)
print(
    so.shortestPathBinaryMatrix([[0, 1, 0, 1, 0], [1, 0, 0, 0, 1], [0, 0, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 0]]),
    6)
