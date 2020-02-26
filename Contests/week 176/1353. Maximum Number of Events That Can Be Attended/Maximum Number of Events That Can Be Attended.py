#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Number of Events That Can Be Attended
@time: 2020/2/26 15:11
"""


class Solution:
    def maxEvents(self, events: list(list())) -> int:
        events = sorted(events, key=lambda x: x[1])
        final = events[-1][1]
        availables = [False] * (final + 1)
        ret = 0
        for e in events:
            for d in range(e[0], e[1] + 1):
                if not availables[d]:
                    availables[d] = True
                    ret += 1
                    break
        return ret


so = Solution()
print(so.maxEvents(events=[[1, 2], [2, 3], [3, 4]]))
print(so.maxEvents(events=[[1, 2], [2, 3], [3, 4], [1, 2]]))
print(so.maxEvents(events=[[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]))
print(so.maxEvents(events=[[1, 100000]]))
print(so.maxEvents(events=[[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]))
