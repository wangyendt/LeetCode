#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Finding the Users Active Minutes
@time: 2021/04/04 10:35
"""

from typing import *
import collections


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res1 = collections.defaultdict(set)
        for l1, l2 in logs:
            res1[l1].add(l2)
        uam = collections.defaultdict(int)
        for key, val in res1.items():
            uam[len(val)] += 1
        ret = [0 for _ in range(k)]
        # print(ret, uam, res1)
        for i in range(k):
            ret[i] = uam[i + 1]
        return ret


so = Solution()
print(so.findingUsersActiveMinutes(logs=[[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], k=5))
