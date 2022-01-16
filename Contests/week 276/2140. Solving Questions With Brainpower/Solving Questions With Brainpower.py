#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Solving Questions With Brainpower.py 
@time: 2022/01/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import functools


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dp(i):
            if i >= len(questions): return 0
            pt, skip = questions[i]
            return max(dp(i + 1), pt + dp(i + skip + 1))

        return dp(0)


so = Solution()
print(so.mostPoints(questions=[[3, 2], [4, 3], [4, 4], [2, 5]]))
print(so.mostPoints(questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
