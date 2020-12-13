#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Partitioning Into Minimum Number Of Deci-Binary Numbers
@time: 2020/12/13 10:33
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(k) for k in n)
