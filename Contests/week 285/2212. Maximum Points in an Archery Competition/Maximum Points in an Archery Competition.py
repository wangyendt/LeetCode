#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Points in an Archery Competition.py 
@time: 2022/03/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *

import functools


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        @functools.lru_cache(None)
        def dp(k, numArrows):
            if k == 12 or numArrows <= 0:
                return 0

            maxScore = dp(k + 1, numArrows)  # Bob Lose
            if numArrows > aliceArrows[k]:
                maxScore = max(maxScore, dp(k + 1, numArrows - aliceArrows[k] - 1) + k)  # Bob Win
            return maxScore

        # backtracking
        ans = [0] * 12
        remainBobArrows = numArrows
        for k in range(12):
            if dp(k, numArrows) != dp(k + 1, numArrows):  # If Bob win
                ans[k] = aliceArrows[k] + 1
                numArrows -= ans[k]
                remainBobArrows -= ans[k]

        ans[0] += remainBobArrows  # In case of having remain arrows then it means in all sections Bob always win
        # then we can distribute the remain to any section, here we simple choose first section.
        return ans
