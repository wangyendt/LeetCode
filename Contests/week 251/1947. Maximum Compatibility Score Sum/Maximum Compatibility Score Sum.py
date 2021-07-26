#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Compatibility Score Sum.py 
@time: 2021/07/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
from itertools import permutations


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)

        dp = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                dp[i][j] = sum(x == y for x, y in zip(students[i], mentors[j]))

        ans = 0
        for perm in permutations(range(m)):
            ans = max(ans, sum(dp[i][j] for i, j in zip(perm, range(m))))
        return ans
