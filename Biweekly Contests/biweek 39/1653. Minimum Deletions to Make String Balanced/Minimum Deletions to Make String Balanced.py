#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Deletions to Make String Balanced.py 
@time: 2020/11/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        cnt_b = 0
        for i in range(1, len(s) + 1):
            if s[i - 1] == 'b':
                dp[i] = dp[i - 1]
                cnt_b += 1
            else:
                dp[i] = min(
                    cnt_b, 1 + dp[i - 1]
                )

        return dp[-1]


so = Solution()
print(so.minimumDeletions("aababbab"))
