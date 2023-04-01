#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/17 10:43
@Author:  wang121ye
@File: People Whose List of Favorite Companies Is Not a Subset of Another List.py
@Software: PyCharm
"""

import collections
import functools


class Solution:
    def peopleIndexes(self, favoriteCompanies: list(list())) -> list:
        dic = collections.defaultdict(set)
        for fci, fcs in enumerate(favoriteCompanies):
            for fc in fcs:
                dic[fc].add(fci)
        ret = []
        for fci, fcs in enumerate(favoriteCompanies):
            # for fc in fcs:
            res = list(functools.reduce(lambda x, y: x & y, [dic[fc] for fc in fcs]))
            res.remove(fci)
            if not res: ret.append(fci)
        return ret


so = Solution()
print(so.peopleIndexes(
    [["leetcode", "google", "facebook"], ["google", "microsoft"], ["google", "facebook"], ["google"], ["amazon"]]))
print(so.peopleIndexes([["leetcode", "google", "facebook"], ["leetcode", "amazon"], ["facebook", "google"]]))
print(so.peopleIndexes([["leetcode"], ["google"], ["facebook"], ["amazon"]]))
