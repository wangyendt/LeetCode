#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Path Crossing
@time: 2020/06/28 10:30
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        stack = {(0, 0): 1}
        for p in path:
            if p == 'N':
                y += 1
            elif p == 'E':
                x += 1
            elif p == 'S':
                y -= 1
            elif p == 'W':
                x -= 1
            if (x, y) in stack:
                return True
            stack[(x, y)] = 1
        return False


so = Solution()
print(so.isPathCrossing('NES'))
print(so.isPathCrossing('NESWW'))
print(so.isPathCrossing('NNNNN' * 20000))
