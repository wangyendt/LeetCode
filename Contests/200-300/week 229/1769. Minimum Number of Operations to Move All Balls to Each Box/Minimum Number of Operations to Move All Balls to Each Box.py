#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Operations to Move All Balls to Each Box.py 
@time: 2021/02/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        dp1 = [0] * n
        dp2 = [0] * n
        cnt = 0
        for i in range(n):
            if i > 0:
                dp1[i] = dp1[i - 1] + cnt
            if boxes[i] == '1':
                cnt += 1
        cnt = 0
        for i in range(n)[::-1]:
            if i < n - 1:
                dp2[i] = dp2[i + 1] + cnt
            if boxes[i] == '1':
                cnt += 1
        return [d1 + d2 for d1, d2 in zip(dp1, dp2)]


so = Solution()
print(so.minOperations(boxes="001011"))
