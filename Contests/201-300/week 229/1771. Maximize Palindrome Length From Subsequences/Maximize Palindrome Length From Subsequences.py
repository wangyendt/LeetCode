#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximize Palindrome Length From Subsequences.py 
@time: 2021/02/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        word = word1 + word2
        n = len(word)
        ans = 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif word[i] == word[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if i < len(word1) <= j:  # Check if this palindrome begins with word1[i] and ends with word2[j]
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return ans
