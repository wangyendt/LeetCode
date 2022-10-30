#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Rank Transform of an Array
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/27 17:04
@Desc   ：
=================================================="""

import collections


class Solution:
    def arrayRankTransform(self, arr: list) -> list:
        A = sorted(list(set(arr)))
        rank = collections.defaultdict(int)
        for i, a in enumerate(A):
            rank[a] = i + 1
        ret = []
        for a in arr:
            ret.append(rank[a])
        return ret


so = Solution()
print(so.arrayRankTransform(arr=[40, 10, 20, 30]))
print(so.arrayRankTransform(arr=[100, 100, 100]))
print(so.arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]))
