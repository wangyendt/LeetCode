#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Alert Using Same Key-Card Three or More Times in a One Hour Period
@time: 2020/10/03 22:41
"""

from typing import *
import collections


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def transfer(s: str) -> int:
            return int(s[:2]) * 60 + int(s[-2:])

        A = collections.defaultdict(list)
        for n, t in zip(keyName, keyTime):
            A[n].append(transfer(t))
        ret = set()
        # print(A)
        for key, val in A.items():
            val.sort()
            for k in range(len(val)):
                if k >= 2:
                    # print(key, val[k - 2], val[k - 1], val[k])
                    if val[k - 2] < val[k - 1] < val[k] <= val[k - 2] + 60:
                        ret.add(key)
                        break
        return sorted(list(ret))


so = Solution()
# print(so.alertNames(keyName=["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
#                     keyTime=["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]))
print(so.alertNames(["a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b"],
                    ["23:27", "03:14", "12:57", "13:35", "13:18", "21:58", "22:39", "10:49", "19:37", "14:14",
                     "10:41"]))
