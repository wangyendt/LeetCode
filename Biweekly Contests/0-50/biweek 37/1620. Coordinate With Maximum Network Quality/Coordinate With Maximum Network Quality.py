#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Coordinate With Maximum Network Quality
@time: 2020/10/18 19:53
"""

from typing import *
import math


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        M, Mx, My = float('-inf'), 0, 0
        for c in range(51):
            for r in range(51):
                sq = 0
                for x, y, q in towers:
                    d = math.dist((x, y), (c, r))
                    if d <= radius: sq += int(q / (1 + d))
                if sq > M:
                    M, Mx, My = sq, c, r
        return [Mx, My]
