#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
@time: 2020/05/31 10:35
"""


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list, verticalCuts: list) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        h_max = max(
            horizontalCuts[0],
            h - horizontalCuts[-1],
            max([horizontalCuts[i] - horizontalCuts[i - 1] for i in range(1, len(horizontalCuts))] + [0])
        )
        w_max = max(
            verticalCuts[0],
            w - verticalCuts[-1],
            max([verticalCuts[i] - verticalCuts[i - 1] for i in range(1, len(verticalCuts))] + [0])
        )
        # print(h_max, w_max)
        return (h_max * w_max) % (10 ** 9 + 7)


so = Solution()
print(so.maxArea(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]))
print(so.maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]))
print(so.maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3]))
print(so.maxArea(h=500000, w=400000, horizontalCuts=[3], verticalCuts=[3]))
