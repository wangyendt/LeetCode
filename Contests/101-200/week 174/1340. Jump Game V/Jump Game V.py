#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Jump Game V
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/2/21 17:20
@Desc   ：
=================================================="""


class Solution:
    def maxJumps(self, arr: list, d: int) -> int:
        n = len(arr)
        res = [0] * n

        def dp(i):
            if res[i]: return res[i]
            res[i] = 1
            for di in [-1, 1]:
                for j in range(i + di, i + di + d * di, di):
                    if not (0 <= j < n and arr[i] > arr[j]): break
                    res[i] = max(res[i], dp(j) + 1)
            return res[i]

        return max(map(dp, range(n)))


so = Solution()
print(so.maxJumps(arr=[6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], d=2))
print(so.maxJumps(arr=[3, 3, 3, 3, 3], d=3))
print(so.maxJumps(arr=[7, 6, 5, 4, 3, 2, 1], d=1))
print(so.maxJumps(arr=[7, 1, 7, 1, 7, 1], d=2))
print(so.maxJumps(arr=[66], d=1))
