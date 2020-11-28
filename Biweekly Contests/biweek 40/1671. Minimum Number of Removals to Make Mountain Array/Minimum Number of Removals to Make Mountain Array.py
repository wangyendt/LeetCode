#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Number of Removals to Make Mountain Array
@time: 2020/11/28 23:11
"""

from typing import *
import math


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def lis_length_dp_nlogn(t: List[int]):
            arr = []
            i = 0
            while i < len(t):
                if i == 0:
                    arr.append(t[0])
                else:
                    boo = True
                    low = 0
                    heigh = len(arr) - 1
                    while low <= heigh:
                        mid = math.floor((low + heigh) / 2)
                        if arr[mid] < t[i]:
                            low = mid + 1
                        if arr[mid] >= t[i]:
                            if mid == 0 or arr[mid - 1] < t[i]:
                                arr[mid] = t[i]
                                boo = False
                                break
                            if arr[mid - 1] == t[i]:
                                boo = False
                                break
                            else:
                                heigh = mid - 1
                    if boo:
                        arr.append(t[i])
                i += 1
                yield len(arr)

        dp1 = list(lis_length_dp_nlogn(nums))
        dp2 = list(lis_length_dp_nlogn(nums[::-1]))[::-1]
        s = max(d1 + d2 for i, (d1, d2) in enumerate(zip(dp1, dp2)) if 0 < i < len(nums) - 1)
        return len(nums) + 1 - s


so = Solution()
print(so.minimumMountainRemovals(nums=[2, 1, 1, 5, 6, 2, 3, 1]))
print(so.minimumMountainRemovals([9, 8, 1, 7, 6, 5, 4, 3, 2, 1]))
