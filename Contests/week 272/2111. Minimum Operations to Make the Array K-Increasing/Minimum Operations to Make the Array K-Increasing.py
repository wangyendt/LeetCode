#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Operations to Make the Array K-Increasing.py 
@time: 2021/12/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def helper(arr: list):
            res = []
            for i, a in enumerate(arr):
                if not res or res[-1] <= a:
                    res.append(a)
                else:
                    idx = bisect.bisect_right(res, a)
                    res[idx] = a
            return len(res)

        n = len(arr)
        ans = 0
        for i in range(k):
            newArr = []
            for j in range(i, n, k):
                newArr.append(arr[j])
            ans += len(newArr) - helper(newArr)
        return ans
