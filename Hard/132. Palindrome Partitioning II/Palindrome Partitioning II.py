#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Palindrome Partitioning II.py 
@time: 2019/07/02
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import sys


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i - 1 for i in range(0, n + 1)]  # dp[i]: the minimum cuts needed for s[:i]
        for i in range(0, n + 1):
            j = 0
            while i - j >= 0 and i + j < n and s[i + j] == s[i - j]:
                dp[i + j + 1] = min(dp[i + j + 1], dp[i - j] + 1)
                j += 1
            j = 1
            while i - j + 1 >= 0 and i + j < n and s[i - j + 1] == s[i + j]:
                dp[i + j + 1] = min(dp[i + j + 1], dp[i - j + 1] + 1)
                j += 1
        return dp[n]


so = Solution()
print(so.minCut('a'), 0)
print(so.minCut('aab'), 1)
print(so.minCut("abaa"), 1)
print(so.minCut('abcaaa'), 3)
test = 'a' * 701 + 'bb' + 'a' * 700
print(test)
print(so.minCut(test))
