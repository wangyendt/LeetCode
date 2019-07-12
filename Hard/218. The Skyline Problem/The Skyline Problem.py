# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/11 17:09
# software: PyCharm


import bisect
from collections import defaultdict


class Solution:
    def getSkyline(self, buildings: list(list())) -> list(list()):
        if not buildings: return []
        buildingsDict = defaultdict(int)
        for b in buildings:
            buildingsDict[(b[0], b[1])] = max(buildingsDict[(b[0], b[1])], b[2])
        buildings = [(v, k[0], k[1]) for k, v in buildingsDict.items()]
        priorityQueue = []
        ret = set()
        for b in buildings:
            if not priorityQueue:
                ret.add((b[1], b[0]))
            else:
                nh, nl, nr = b
                ch, cl, cr = priorityQueue[-1]
                most_right = cr
                while priorityQueue:
                    ph, pl, pr = priorityQueue[-1]
                    most_right = max(most_right, pr)
                    if pr >= nl:
                        if pr == nl and ph != nh:
                            ret.add((pr, nh))
                        break
                    else:
                        priorityQueue.pop()
                        if pr > cr:
                            ret.add((cr, ph))
                            cl, cr, ch = pl, pr, ph
                        if not priorityQueue:
                            ret.add((most_right, 0))
                            ret.add((nl, nh))
                if nl <= cr and nh > ch:
                    ret.add((nl, nh))
            bisect.insort(priorityQueue, b)
        ch, cl, cr = priorityQueue[-1]
        most_right = 0
        while priorityQueue:
            ph, pl, pr = priorityQueue.pop()
            most_right = max(most_right, pr)
            if pr > cr:
                ret.add((cr, ph))
                cl, cr, ch = pl, pr, ph
            if not priorityQueue:
                ret.add((most_right, 0))
        return sorted(list(map(list, ret)), key=lambda x: x[0])


so = Solution()
# print(so.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]),
#       [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])
# print(so.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]]))
# print(so.getSkyline([[0, 5, 7], [5, 10, 7], [5, 10, 12], [10, 15, 7], [15, 20, 7], [15, 20, 12], [20, 25, 7]]))
# print([[0, 7], [5, 12], [10, 7], [15, 12], [20, 7], [25, 0]])
print(so.getSkyline([[2, 4, 70], [3, 8, 30], [6, 100, 41], [7, 15, 70],
                     [10, 30, 102], [15, 25, 76], [60, 80, 91], [70, 90, 72], [85, 120, 59]]))
print([[2, 70], [4, 30], [6, 41], [7, 70], [10, 102], [30, 41], [60, 91], [80, 72], [90, 59], [120, 0]])
