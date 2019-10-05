# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/8 0:46
# software: PyCharm


class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, side: int, maxOnes: int) -> int:
        # Solution: Fold Matrix
        # Take 7*5, side=3, maxOnes=3 as example:
        # . . .|. . .|.                 1 1 .|1 1 .|1
        # . . .|. . .|. fold  6 4 4     1 . .|1 . .|1
        # . . .|. . .|. ----\ 6 4 4 ==> . . .|. . .|.
        # ------------- ----/ 3 2 2     -------------
        # . . .|. . .|.         ||      1 1 .|1 1 .|1
        # . . .|. . .|.         \/      1 . .|1 . .|1
        #                  6+6+4 = 16

        # Matrix Horizontal [:] -> [..]
        if width < height:
            width, height = height, width

        # Fold
        x, x0 = divmod(width, side)
        v, v0 = divmod(height, side)
        count = [x0 * v0, (side - x0) * v0,
                 x0 * (side - v0), (side - x0) * (side - v0)
                 ]

        value = [(x + 1) * (v + 1), x * (v + 1),
                 (x + 1) * v, x * v,
                 ]

        # Sum the largest ones
        ans = 0
        for k, n in zip(count, value):
            if maxOnes > k:
                ans += k * n
                maxOnes -= k
            else:
                return ans + maxOnes * n
        return ans
