#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Visible People in a Queue.py 
@time: 2021/07/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []
        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] <= v:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        return res


so = Solution()
print(so.canSeePersonsCount(heights=[10, 6, 8, 5, 11, 9]))
