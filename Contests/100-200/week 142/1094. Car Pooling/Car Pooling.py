# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/25 1:25
# software: PyCharm


class Solution:
    def carPooling(self, trips: list(list()), capacity: int) -> bool:
        if not trips: return True
        start = sorted(trips, key=lambda x: x[1])
        end = sorted(trips, key=lambda x: x[2])
        print(start)
        print(end)
        pStart, pEnd = 0, 0
        for i in range(1, start[-1][1] + 1):
            while start and i == start[pStart][1]:
                capacity -= start[0][0]
                start.pop(0)
            while end and i == end[pEnd][2]:
                capacity += end[0][0]
                end.pop(0)
            if capacity < 0:
                return False
        return True


so = Solution()
print(so.carPooling([[2, 1, 5], [3, 3, 7]], 4), False)
