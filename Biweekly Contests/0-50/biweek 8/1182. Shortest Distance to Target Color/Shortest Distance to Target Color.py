# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/8 0:03
# software: PyCharm


import bisect
import collections


class Solution:
    def shortestDistanceColor(self, colors: list, queries: list(list())) -> list:
        def take_closest(myList, myNumber):
            pos = bisect.bisect_left(myList, myNumber)
            if pos == 0:
                return myList[0]
            if pos == len(myList):
                return myList[-1]
            before = myList[pos - 1]
            after = myList[pos]
            if after - myNumber < myNumber - before:
                return after
            else:
                return before
        ret = []
        d1, d2 = collections.defaultdict(list), collections.defaultdict(list)
        prev = 0
        for ci, c in enumerate(colors):
            if c != prev:
                d1[c].append(ci)
            prev = c
        prev = 0
        for ci, c in enumerate(colors[::-1]):
            if c != prev:
                d2[c].insert(0, len(colors) - 1 - ci)
            prev = c
        for q_ind, q in queries:
            if not d1[q] and not d2[q]:
                ret.append(-1)
                continue
            if colors[q_ind] == q:
                ret.append(0)
            else:
                res = len(colors)
                res = min(res, abs(q_ind-take_closest(d1[q],q_ind)))
                res = min(res, abs(q_ind-take_closest(d2[q],q_ind)))
                ret.append(res)
        return ret


so = Solution()
print(so.shortestDistanceColor(colors=[1, 1, 2, 1, 3, 2, 2, 3, 3], queries=[[1, 3], [2, 2], [6, 1]]))
print(so.shortestDistanceColor(colors=[1, 2], queries=[[0, 3]]))
print(so.shortestDistanceColor([2, 1, 2, 2, 1],
                               [[1, 1], [4, 3], [1, 3], [4, 2], [2, 1]]))
