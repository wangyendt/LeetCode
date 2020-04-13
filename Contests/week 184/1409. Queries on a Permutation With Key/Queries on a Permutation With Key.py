#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/12 10:38
@Author:  wang121ye
@File: Queries on a Permutation With Key.py
@Software: PyCharm
"""


class Solution:
    def processQueries(self, queries: list, m: int) -> list:
        arr = list(range(1, m + 1))
        ret = []
        for q in queries:
            ind = arr.index(q)
            ret.append(ind)
            arr.pop(ind)
            arr.insert(0, q)
        return ret


so = Solution()
print(so.processQueries(queries=[3, 1, 2, 1], m=5))
print(so.processQueries(queries=[4, 1, 2, 2], m=4))
print(so.processQueries(queries=[7, 5, 5, 8, 3], m=8))
