#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Slowest Key
@time: 2020/10/25 10:33
"""

from typing import *
import collections


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes = [0] + releaseTimes
        res = collections.defaultdict(int)
        for idx, key in enumerate(keysPressed):
            res[key] = max(res[key], releaseTimes[idx + 1] - releaseTimes[idx])
        res = [(k, v) for k, v in res.items()]
        print(res)
        res = sorted(res, key=lambda x: (x[1], x[0]))
        return res[-1][0]


so = Solution()
print(so.slowestKey(releaseTimes=[12, 23, 36, 46, 62], keysPressed="spuda"))
