#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Shortest Subarray to be Removed to Make Array Sorted.py 
@time: 2020/09/05
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import bisect


class Solution:
    def findLengthOfShortestSubarray(self, arr: list) -> int:
        n = len(arr)
        l, r = 1, 1
        if n == 1: return 0
        if arr == sorted(arr): return 0
        for i in range(n):
            if i:
                if arr[i] >= arr[i - 1]:
                    l += 1
                else:
                    break
        for i in range(n)[::-1]:
            if i < len(arr) - 1:
                if arr[i] <= arr[i + 1]:
                    r += 1
                else:
                    break
        if arr[l - 1] <= arr[n - r]: return n - l - r
        p, q = l - 1, n - r
        ret = 0
        for i in range(p + 1)[::-1]:
            idx = bisect.bisect_left(arr[q:], arr[i])
            ret = max(ret, n - q - idx + i + 1)
            if arr[i] <= arr[q]: break
        for i in range(q, n):
            idx = bisect.bisect_right(arr[:p + 1], arr[i])
            ret = max(ret, idx + n - i)
            if arr[p] <= arr[i]: break
        return max(0, n - ret)


so = Solution()
print(so.findLengthOfShortestSubarray(arr=[1, 2, 3, 10, 4, 2, 3, 5]))
print(so.findLengthOfShortestSubarray([1, 2, 3]))
print(so.findLengthOfShortestSubarray([1]))
