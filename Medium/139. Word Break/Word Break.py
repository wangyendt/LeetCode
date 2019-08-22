#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Word Break
@time: 2019/8/22 16:04
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for w in wordDict:
                if s[i - len(w):i] == w and dp[i - len(w)]:
                    dp[i] = True
                    break
        return dp[-1]


so = Solution()
print(so.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
