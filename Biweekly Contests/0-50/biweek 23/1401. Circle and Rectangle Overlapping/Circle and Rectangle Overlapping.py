#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Circle and Rectangle Overlapping.py 
@time: 2020/04/08
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def min_dist_from_point_to_segment(point, left, right, height):
            x, y = point
            if left <= x <= right:
                return (y - height) ** 2
            else:
                return min((x - left) ** 2 + (y - height) ** 2, (x - right) ** 2 + (y - height) ** 2)

        return x1 <= x_center <= x2 and y1 <= y_center <= y2 or min(
            min_dist_from_point_to_segment((xc, yc), l, r, h)
            for xc, yc, l, r, h in zip(
                [x_center, x_center, y_center, y_center],
                [y_center, y_center, x_center, x_center],
                [x1, x1, y1, y1], [x2, x2, y2, y2], [y1, y2, x1, x2]
            )) <= radius ** 2


so = Solution()
print(so.checkOverlap(radius=1, x_center=0, y_center=0, x1=1, y1=-1, x2=3, y2=1))
print(so.checkOverlap(radius=1, x_center=0, y_center=0, x1=-1, y1=0, x2=0, y2=1))
print(so.checkOverlap(radius=1, x_center=1, y_center=1, x1=-3, y1=-3, x2=3, y2=3))
print(so.checkOverlap(radius=1, x_center=1, y_center=1, x1=1, y1=-3, x2=2, y2=-1))
print(so.checkOverlap(4, 102, 50, 0, 0, 100, 100))
