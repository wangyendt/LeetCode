#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> XOR Queries of a Subarray
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/7 17:11
@Desc   ：
=================================================="""


class Solution:
    def xorQueries(self, arr: list, queries: list(list())) -> list:
        res = [0]
        last = 0
        for a in arr:
            res.append(last ^ a)
            last = last ^ a
        ret = []
        for qa, qb in queries:
            if qa == qb:
                ret.append(arr[qa])
            else:
                ret.append(res[qb + 1] ^ res[qa])
        return ret


so = Solution()
print(so.xorQueries(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]))
print(so.xorQueries(arr=[4, 8, 2, 10], queries=[[2, 3], [1, 3], [0, 0], [0, 3]]))
