#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Longest Ideal Subsequence.py 
@time: 2022/09/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 128
        for c in s:
            i = ord(c)
            dp[i] = max(dp[i - k: i + k + 1]) + 1
        return max(dp)


so = Solution()
print(so.longestIdealString(s="acfgbd", k=2))
print(so.longestIdealString("lkpkxcigcs", 6))
