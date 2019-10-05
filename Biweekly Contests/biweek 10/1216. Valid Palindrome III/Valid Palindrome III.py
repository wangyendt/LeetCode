#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Valid Palindrome III.py 
@time: 2019/10/05
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def isKPalRec(str1, str2, m, n):
            if not m: return n
            if not n: return m
            if str1[m - 1] == str2[n - 1]:
                return isKPalRec(str1, str2, m - 1, n - 1)
            res = 1 + min(isKPalRec(str1, str2, m - 1, n),
                          (isKPalRec(str1, str2, m, n - 1)))
            return res

        def isKPal(s, k):
            revStr = s[::-1]
            l = len(s)
            return isKPalRec(s, revStr, l, l) <= k * 2

        return isKPal(s, k)


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def is_k_pal_dp(str1, str2, m, n):
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m + 1):
                for j in range(n + 1):
                    if not i:
                        dp[i][j] = j
                    elif not j:
                        dp[i][j] = i
                    elif str1[i - 1] == str2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j],
                                           (dp[i][j - 1]))

            return dp[m][n]

        def is_k_pal(s, k):
            revStr = s[::-1]
            l = len(s)

            return is_k_pal_dp(s, revStr, l, l) <= k * 2

        return is_k_pal(s, k)


so = Solution()
print(so.isValidPalindrome(s="abcdeca", k=2))
print(so.isValidPalindrome(s="abcdeca", k=1))
print(so.isValidPalindrome(s="", k=1))
