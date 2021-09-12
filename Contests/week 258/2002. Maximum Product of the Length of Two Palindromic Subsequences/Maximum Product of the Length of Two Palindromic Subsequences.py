#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Product of the Length of Two Palindromic Subsequences.py 
@time: 2021/09/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from itertools import chain, combinations


class Solution:
    def maxProduct(self, s: str) -> int:
        def powerset(iterable):
            xs = list(iterable)
            return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))

        def is_palindrome(arr):
            for i in range((len(arr) + 1) // 2):
                if s[arr[i]] != s[arr[~i]]:
                    break
            else:
                return True
            return False

        def longestPalindromeSubseq(s):
            if s == s[::-1]:
                return len(s)

            n = len(s)
            dp = [[0 for j in range(n)] for i in range(n)]

            for i in range(n - 1, -1, -1):
                dp[i][i] = 1
                for j in range(i + 1, n):
                    if s[i] == s[j]:
                        dp[i][j] = 2 + dp[i + 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

            return dp[0][n - 1]

        ss = set(list(range(len(s))))
        ret = 0
        for t in powerset(list(range(len(s)))):
            if not t: continue
            if is_palindrome(t):
                s2 = ''.join([s[tt] for tt in sorted(ss - set(t))])
                if not s2: break
                # print(len(t), longestPalindromeSubseq(s2), ''.join([s[ttt] for ttt in t]), s2)
                ret = max(ret, len(t) * longestPalindromeSubseq(s2))
        return ret


so = Solution()
print(so.maxProduct("leetcodecom"))
print(so.maxProduct("bb"))
print(so.maxProduct("yyye"))
print(so.maxProduct("nphnphmpm"))
