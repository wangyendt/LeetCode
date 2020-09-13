#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count Unhappy Friends
@time: 2020/09/13 10:44
"""

import collections


class Solution:
    def unhappyFriends(self, n: int, A: list(list()), pairs: list(list())) -> int:
        mems = collections.defaultdict(int)

        def find(k1, k2):
            if (k1, k2) not in mems:
                mems[(k1, k2)] = A[k1].index(k2)
            return mems[(k1, k2)]

        res = set()
        for p1, p2 in pairs:
            for q1, q2 in pairs:
                if not (p1 == q1 and p2 == q2):
                    if find(p1, q1) < find(p1, p2) and find(q1, p1) < find(q1, q2):
                        res.add(p1)
                    if find(p2, q1) < find(p2, p1) and find(q1, p2) < find(q1, q2):
                        res.add(p2)
                    if find(p1, q2) < find(p1, p2) and find(q2, p1) < find(q2, q1):
                        res.add(p1)
                    if find(p2, q2) < find(p2, p1) and find(q2, p2) < find(q2, q1):
                        res.add(p2)
        return len(res)


so = Solution()
print(so.unhappyFriends(n=4, A=[[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs=[[0, 1], [2, 3]]))
print(so.unhappyFriends(n=4, A=[[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs=[[1, 3], [0, 2]]))
