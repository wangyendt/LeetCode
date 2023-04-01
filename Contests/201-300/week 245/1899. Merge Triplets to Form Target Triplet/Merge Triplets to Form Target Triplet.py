#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Merge Triplets to Form Target Triplet
@time: 2021/06/13 23:02
"""


class Solution:
    def mergeTriplets(self, triplets, T):
        forbidden = set()
        for i, [x, y, z] in enumerate(triplets):
            if x > T[0] or y > T[1] or z > T[2]:
                forbidden.add(i)

        a, b, c = 0, 0, 0
        for i, (x, y, z) in enumerate(triplets):
            if i not in forbidden:
                a, b, c = max(a, x), max(b, y), max(c, z)

        return [a, b, c] == T
