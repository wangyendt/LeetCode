#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Operations to Make Array Equal
@time: 2020/08/16 23:48
"""


class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2:
            return (n + 1) * (n // 2) // 2
        else:
            return n * (n // 2) // 2
