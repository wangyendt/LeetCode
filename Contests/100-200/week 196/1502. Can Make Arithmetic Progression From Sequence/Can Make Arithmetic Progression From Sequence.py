#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Can Make Arithmetic Progression From Sequence
@time: 2020/07/05 10:31
"""


class Solution:
    def canMakeArithmeticProgression(self, arr: list) -> bool:
        arr.sort()
        diff = arr[0] - arr[1]
        return all(diff == arr[i] - arr[i + 1] for i in range(0, len(arr) - 1))
