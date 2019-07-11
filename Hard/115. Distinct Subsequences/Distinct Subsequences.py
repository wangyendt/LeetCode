# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/19 22:39
# software: PyCharm

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for i in range(len(s)):
            for j in range(len(t))[::-1]:
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[-1]


so = Solution()
print(so.numDistinct("rabbbit", "rabbit"), 3)
