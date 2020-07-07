#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Self Crossing
@time: 2020/7/7 16:01
"""

import sys
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y + other.y)

    @staticmethod
    def cross_trial(p1, p2, p3):
        return (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y)

    def __str__(self):
        return f'x:{self.x}, y:{self.y}'


class Solution:
    def isSelfCrossing(self, x: list) -> bool:
        def cross(seg1, seg2):
            A, B = Point(*seg1[:2]), Point(*seg1[2:])
            C, D = Point(*seg2[:2]), Point(*seg2[2:])
            if (min(A.x, B.x) <= max(C.x, D.x) and
                    min(C.x, D.x) <= max(A.x, B.x) and
                    min(A.y, B.y) <= max(C.y, D.y) and
                    min(C.y, D.y) <= max(A.y, B.y)):
                if (Point.cross_trial(A, B, C) * Point.cross_trial(A, B, D) <= 0
                        and Point.cross_trial(C, D, A) * Point.cross_trial(C, D, B) <= 0):
                    return True
                else:
                    return False
            else:
                return False

        def cross_n(s1, s2_n):
            return any(cross(s1, _) for _ in s2_n)

        direction = lambda p, q: {
            0: (0, q), 1: (-q, 0), 2: (0, -q), 3: (q, 0)
        }[p]
        xs, ys = 0, 0
        stack = []
        # plt.figure()
        # plt.ion()
        for i in range(len(x)):
            delta = direction(i % 4, x[i])
            xn, yn = xs + delta[0], ys + delta[1]
            stack.append((xs, ys, xn, yn))
            # if i % 2 == 0:
            #     plt.vlines(xs, min(ys, yn), max(ys, yn))
            # else:
            #     plt.hlines(ys, min(xs, xn), max(xs, xn))
            # plt.pause(1)
            xs, ys = xn, yn
            if len(stack) >= 4:
                # print(stack)
                is_cross = cross_n(stack[-1], stack[:-2])
                if is_cross: return True
            if len(stack) >= 6:
                stack.pop(0)
        # plt.close()
        return False


so = Solution()
print(so.isSelfCrossing([1, 1, 2, 1, 1]))
print(so.isSelfCrossing([2, 1, 1, 2]))
print(so.isSelfCrossing([1, 2, 3, 4]))
print(so.isSelfCrossing([1, 1, 1, 1]))
print(so.isSelfCrossing([1, 1, 2, 2, 3, 3, 4, 4, 10, 4, 4, 3, 3, 2, 2, 1, 1]))
