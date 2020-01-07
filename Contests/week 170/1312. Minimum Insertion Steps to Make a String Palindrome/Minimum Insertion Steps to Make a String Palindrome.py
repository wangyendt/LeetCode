#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Minimum Insertion Steps to Make a String Palindrome
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/7 18:25
@Desc   ：
=================================================="""


class Solution:
    def minInsertions(self, s):
        n = len(s)
        dp = [[0] * (n + 1) for i in range(n + 1)]
        for i in range(n):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j] + 1 if s[i] == s[~j] else max(dp[i][j + 1], dp[i + 1][j])
        return n - dp[n][n]


so = Solution()
print(so.minInsertions(s="zzazz"))
print(so.minInsertions(s="mbadm"))
print(so.minInsertions(s="leetcode"))
print(so.minInsertions(s="g"))
print(so.minInsertions(s="no"))
