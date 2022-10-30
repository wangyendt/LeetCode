#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Minimum Difficulty of a Job Schedule
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/26 11:52
@Desc   ：
=================================================="""

import collections


class Solution:
    def minDifficulty(self, jobDifficulty: list, d: int) -> int:
        n, inf = len(jobDifficulty), sum(jobDifficulty)
        if n < d: return -1
        dp = [[0 for _ in range(d + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = max(jobDifficulty[:i])
        # print(n, d)
        max_job_difficulty = collections.defaultdict(int)
        for j in range(2, d + 1):
            for i in range(j, n + 1):
                res = inf
                for k in range(j - 1, i):
                    if (k, i) not in max_job_difficulty:
                        max_job_difficulty[(k, i)] = max(jobDifficulty[k:i])
                    res = min(res, dp[k][j - 1] + max_job_difficulty[(k, i)])
                dp[i][j] = res
        # print(dp)
        return dp[-1][-1]


so = Solution()
# print(so.minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2))
# print(so.minDifficulty(jobDifficulty=[9, 9, 9], d=4))
# print(so.minDifficulty(jobDifficulty=[1, 1, 1], d=3))
# print(so.minDifficulty(jobDifficulty=[7, 1, 7, 1, 7, 1], d=3))
# print(so.minDifficulty(jobDifficulty=[11, 111, 22, 222, 33, 333, 44, 444], d=6))
print(so.minDifficulty(jobDifficulty=list(range(300)), d=10))
