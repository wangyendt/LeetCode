#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Building Height.py 
@time: 2021/04/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maxBuilding(self, n: int, arr: List[List[int]]) -> int:
        arr.extend([[1, 0], [n, n - 1]])
        arr.sort()
        m = len(arr)

        for i in range(1, m):
            arr[i][1] = min(arr[i][1], arr[i - 1][1] + arr[i][0] - arr[i - 1][0])
        for i in range(m - 2, -1, -1):
            arr[i][1] = min(arr[i][1], arr[i + 1][1] + arr[i + 1][0] - arr[i][0])

        ans = 0
        for i in range(1, m):
            l, h1 = arr[i - 1]
            r, h2 = arr[i]
            diff = abs(h1 - h2)
            if r - l < diff:
                ans = max(ans, min(h1, h2) + r - l)
            else:
                ans = max(ans, max(h1, h2) + (r - l - diff) // 2)
        return ans
