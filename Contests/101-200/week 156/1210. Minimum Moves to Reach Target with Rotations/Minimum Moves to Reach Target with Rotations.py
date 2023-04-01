# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/29 12:20
# software: PyCharm


class Solution:
    def minimumMoves(self, grid: list(list())) -> int:
        n = len(grid)
        q = [(0, 0, True)]
        visited = set(q)
        step = 0
        while q:
            newq = []
            for x, y, right in q:
                if x == n - 1 and y == n - 2 and right == True:
                    return step
                if right:
                    x2 = x
                    y2 = y + 1
                else:
                    x2 = x + 1
                    y2 = y
                for dx, dy in [(0, 1), (1, 0)]:
                    newx, newy = x + dx, y + dy
                    newx2, newy2 = x2 + dx, y2 + dy
                    if (0 <= newx < n and 0 <= newy < n and
                            0 <= newx2 < n and 0 <= newy2 < n and
                            grid[newx][newy] == 0 and grid[newx2][newy2] == 0):
                        if (newx, newy, right) not in visited:
                            newq.append((newx, newy, right))
                            visited.add((newx, newy, right))
                if right:
                    if x + 1 < n and grid[x + 1][y] == 0 and grid[x + 1][y + 1] == 0:
                        if (x, y, False) not in visited:
                            newq.append((x, y, False))
                            visited.add((x, y, False))
                else:
                    if y + 1 < n and grid[x][y + 1] == 0 and grid[x + 1][y + 1] == 0:
                        if (x, y, True) not in visited:
                            newq.append((x, y, True))
                            visited.add((x, y, True))

            q = newq
            step += 1

        return -1


so = Solution()
print(so.minimumMoves(grid=[[0, 0, 1, 1, 1, 1],
                            [0, 0, 0, 0, 1, 1],
                            [1, 1, 0, 0, 0, 1],
                            [1, 1, 1, 0, 0, 1],
                            [1, 1, 1, 0, 0, 1],
                            [1, 1, 1, 0, 0, 0]]))
