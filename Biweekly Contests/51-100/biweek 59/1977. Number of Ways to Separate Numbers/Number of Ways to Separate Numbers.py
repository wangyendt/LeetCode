#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Ways to Separate Numbers.py 
@time: 2021/08/21
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(num)
        dp = [[0] * (n + 1) for _ in range(n)]
        if num[0] == '0':
            return 0
        dp[0][1] = 1
        for i in range(1, n):
            dp[i][i + 1] = 1
            for j in range(1, i + 1):
                if num[i - j + 1] != '0':

                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD
                    end = i - j
                    if end >= j - 2 and num[end + 1:i] < num[end - j + 2:end + 1]:
                        dp[i][j] = (dp[i][j] + dp[end][j - 1]) % MOD
                    if end >= j - 1 and num[end + 1:i + 1] >= num[end - j + 1:end + 1]:
                        dp[i][j] = (dp[i][j] + dp[end][j]) % MOD

        return (sum(dp[-1])) % MOD


so = Solution()
# print(so.numberOfCombinations(num="327"))
# print(so.numberOfCombinations(num="094"))
print(so.numberOfCombinations(num="9999999999999"))
