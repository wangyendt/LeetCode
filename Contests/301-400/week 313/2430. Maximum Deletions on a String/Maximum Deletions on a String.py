#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Deletions on a String.py 
@time: 2022/10/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import functools
import sys

sys.setrecursionlimit(100000)


class Solution:
    def deleteString(self, s: str) -> int:

        @functools.lru_cache(None)
        def dp(pos):
            res = 0
            for i in range(1, (n - pos) // 2 + 1):
                for j in range(i):
                    if s[pos + j] != s[pos + j + i]:
                        break
                else:
                    res = max(res, dp(pos + i) + 1)
            return res or 1

        if len(set(s)) == 1: return len(s)
        n = len(s)
        return dp(0)

    def deleteString2(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:
            return n
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            for l in range(1, (n - i) // 2 + 1):
                if s[i: i + l] == s[i + l: i + 2 * l]:
                    dp[i] = max(dp[i], 1 + dp[i + l])

        return dp[0]


so = Solution()
print(so.deleteString(s="abcabcdabc"))
print(so.deleteString(s="aaabaab"))
print(so.deleteString(s="aaaaa"))
print(so.deleteString('b' * 4000))
