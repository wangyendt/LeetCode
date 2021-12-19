#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Smooth Descent Periods of a Stock.py 
@time: 2021/12/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = [1] * len(prices)
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                dp[i] += dp[i - 1]
        return sum(dp)
