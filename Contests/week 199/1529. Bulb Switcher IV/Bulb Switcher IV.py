#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Bulb Switcher IV
@time: 2020/07/27 01:00
"""


class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        init = '0' * n
        ret = 0
        for i in range(n):
            if init[i] == target[i] and ret % 2 or init[i] != target[i] and not ret % 2:
                ret += 1
        return ret
