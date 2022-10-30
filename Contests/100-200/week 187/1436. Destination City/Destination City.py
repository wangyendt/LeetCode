#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/9 17:16
@Author:  wang121ye
@File: Destination City.py
@Software: PyCharm
"""

import collections


class Solution:
    def destCity(self, paths: list(list())) -> str:
        dic = collections.defaultdict(str)
        for p in paths:
            dic[p[0]] = p[1]
        p0 = paths[0][0]
        while True:
            if p0 not in dic: return p0
            p0 = dic[p0]


so = Solution()
print(so.destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
print(so.destCity(paths=[["B", "C"], ["D", "B"], ["C", "A"]]))
