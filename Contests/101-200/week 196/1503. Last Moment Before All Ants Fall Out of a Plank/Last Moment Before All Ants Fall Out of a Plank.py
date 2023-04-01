#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Last Moment Before All Ants Fall Out of a Plank
@time: 2020/07/05 10:33
"""


class Solution:
    def getLastMoment(self, n: int, left: list, right: list) -> int:
        ml, mr = max(left or [0]), min(right or [n])
        return max(ml, n - mr)
