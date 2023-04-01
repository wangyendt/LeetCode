#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Deletions to Make Array Beautiful.py 
@time: 2022/03/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        p = 0
        ret = 0
        stack = []
        for i, n in enumerate(nums):
            if not stack:
                stack.append(n)
            else:
                if len(stack) % 2 == 1:
                    if stack[-1] == n:
                        continue
                    else:
                        stack.append(n)
                else:
                    stack.append(n)
        if len(stack) % 2 == 1:
            stack.pop()
        return len(nums) - len(stack)


so = Solution()
print(so.minDeletion(nums=[1, 1, 2, 2, 3, 3]))
print(so.minDeletion([1, 1, 1, 1, 1, 1]))
print(so.minDeletion([2, 32, 4, 5, 435, 34, 3, 345, 34, 534, 534, 534, 5, 345, 345]))
print(so.minDeletion([1, 1, 1, 1, 1, 2, 2, 2, 2] * 10000))
