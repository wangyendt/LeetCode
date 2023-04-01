#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Candies You Can Get from Boxes
@time: 2019/12/24 11:22
"""


class Solution:
    def maxCandies(self, status: list, candies: list, keys: list(list()), containedBoxes: list(list()),
                   initialBoxes: list) -> int:
        if not initialBoxes: return 0
        boxes = set(initialBoxes)
        keyss = set([i for i, s in enumerate(status) if s == 1])
        res = 0
        while boxes & keyss:
            common = boxes & keyss
            for i in common:
                keyss.remove(i)
                boxes.remove(i)
                res += candies[i]
                keyss |= set(keys[i])
                boxes |= set(containedBoxes[i])
        return res
