#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/26 20:17
@Author:  wang121ye
@File: Diagonal Traverse II.py
@Software: PyCharm
"""


class Solution:
    def findDiagonalOrder(self, A):
        res = []
        for i, r in enumerate(A):
            for j, a in enumerate(r):
                if len(res) <= i + j:
                    res.append([])
                res[i + j].append(a)
        return [a for r in res for a in reversed(r)]
