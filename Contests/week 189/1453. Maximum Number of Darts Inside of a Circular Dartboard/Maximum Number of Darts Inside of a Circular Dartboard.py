#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/17 11:00
@Author:  wang121ye
@File: Maximum Number of Darts Inside of a Circular Dartboard.py
@Software: PyCharm
"""

import math


class Solution:
    def numPoints(self, p: list(list()), r: int) -> int:
        eps = 1e-8

        def dist(p1, p2):
            return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

        def getCircleCenter(p1, p2):
            mid = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
            angle = math.atan2(p1[0] - p2[0], p2[1] - p1[1]);
            d = (r * r - pow(dist(p1, mid), 2)) ** 0.5
            return mid[0] + d * math.cos(angle), mid[1] + d * math.sin(angle)

        N = len(p)
        ans = 1
        for i in range(N):
            for j in range(i + 1, N):
                if dist(p[i], p[j]) > 2 * r: continue
                center = getCircleCenter(p[i], p[j])
                cnt = 0
                for k in range(N):
                    if dist(center, p[k]) < 1.0 * r + eps: cnt += 1
                ans = max(ans, cnt)
        return ans


so = Solution()
print(so.numPoints([[-2, 0], [2, 0], [0, 2], [0, -2]], r=2))
print(so.numPoints([[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], r=5))
print(so.numPoints([[-2, 0], [2, 0], [0, 2], [0, -2]], r=1))
print(so.numPoints([[1, 2], [3, 5], [1, -1], [2, 3], [4, 1], [1, 3]], r=2))
