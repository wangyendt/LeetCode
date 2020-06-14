#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Least Number of Unique Integers after K Removals
@time: 2020/06/14 10:33
"""

import collections


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list, k: int) -> int:
        res = sorted(
            [(k, v) for k, v in collections.Counter(arr).items()], key=lambda x: x[1]
        )
        new_arr = []
        for r in res:
            new_arr += [r[0]] * r[1]
        # print(res, new_arr)
        return len(set(new_arr[k:]))


so = Solution()
print(so.findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1))
print(so.findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3))
