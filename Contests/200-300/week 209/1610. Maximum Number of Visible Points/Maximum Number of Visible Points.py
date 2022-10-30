#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Number of Visible Points
@time: 2020/10/05 09:37
"""

from typing import *
import math
import bisect


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        ret = 0
        for pt in points:
            if pt[0] == location[0] and pt[1] == location[1]:
                points.remove(pt)
                ret += 1
        angles = []
        for x, y in points:
            res = math.atan2(y - location[1], x - location[0])
            if res < 0: res += 2 * math.pi
            angles.append(res)
            angles.append(res + 2 * math.pi)
        angles.sort()
        mx = 0
        # print(angles)
        for i in range(len(points)):
            left = i
            right = bisect.bisect_right(angles, angles[i] + angle * math.pi / 180)
            # print(i, left, right)
            mx = max(mx, right - i)
        return round(ret + mx)


so = Solution()
# print(so.visiblePoints(points=[[2, 1], [2, 2], [3, 4], [1, 1]], angle=90, location=[1, 1]))
# print(so.visiblePoints(points=[[1, 0], [2, 1]], angle=13, location=[1, 1]))
print(so.visiblePoints([[3, 16], [4, 17], [5, 18], [6, 19], [7, 21]], 47, [1, 1]))
