# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/8 11:41
# software: PyCharm


class Solution:
    def distanceBetweenBusStops(self, distance: list, start: int, destination: int) -> int:
        if start == destination: return 0
        if start > destination: start, destination = destination, start
        path1 = sum(distance[start:destination])
        path2 = sum(distance) - path1
        return min(path1, path2)


so = Solution()
print(so.distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=1))
print(so.distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=2))
print(so.distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=3))
