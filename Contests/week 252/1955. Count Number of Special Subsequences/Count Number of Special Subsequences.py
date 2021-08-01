#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Number of Special Subsequences.py 
@time: 2021/08/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countSpecialSubsequences(self, A: List[int]) -> int:
        dp = [1, 0, 0, 0]
        for a in A:
            dp[a + 1] += dp[a] + dp[a + 1]
        return dp[-1] % (10 ** 9 + 7)
