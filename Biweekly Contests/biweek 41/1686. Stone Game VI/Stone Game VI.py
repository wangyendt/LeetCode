#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Stone Game VI
@time: 2020/12/12 22:44
"""

from typing import *
import numpy as np


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        res = [a + b for a, b in zip(aliceValues, bobValues)]
        amax = np.argsort(res)
        score = 0
        for i, a in enumerate(amax):
            if i % 2 == 0:
                score += aliceValues[amax[-1 - i]]
            else:
                score -= bobValues[amax[-1 - i]]
        if score > 0:
            return 1
        elif score == 0:
            return 0
        elif score < 0:
            return -1


so = Solution()
print(so.stoneGameVI(aliceValues=[1, 3], bobValues=[2, 1]))
print(so.stoneGameVI(aliceValues=[1, 2], bobValues=[3, 1]))
print(so.stoneGameVI(aliceValues=[2, 4, 3], bobValues=[1, 6, 7]))
print(so.stoneGameVI([9, 8, 3, 8], [10, 6, 9, 5]))
