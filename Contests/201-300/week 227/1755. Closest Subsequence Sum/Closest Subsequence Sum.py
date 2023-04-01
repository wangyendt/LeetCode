#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Closest Subsequence Sum.py 
@time: 2021/02/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        # function that generates all possible sums of sebsequences
        def dfs(i, cur, arr, sums):
            if i == len(arr):
                sums.add(cur)
                return
            dfs(i + 1, cur, arr, sums)
            dfs(i + 1, cur + arr[i], arr, sums)

        sums1, sums2 = set(), set()
        # generate all possible sums of the 1st and 2nd half
        dfs(0, 0, nums[:len(nums) // 2], sums1)
        dfs(0, 0, nums[len(nums) // 2:], sums2)

        # sort the possible sums of the 2nd half
        s2 = sorted(sums2)
        ans = 10 ** 10
        # for each possible sum of the 1st half, find the sum in the 2nd half
        # that gives a value closest to the goal using binary search
        for s in sums1:
            remain = goal - s
            # binary search for the value in s2 that's closest to the remaining value
            i2 = bisect.bisect_left(s2, remain)
            if i2 < len(s2):
                ans = min(ans, abs(remain - s2[i2]))
            if i2 > 0:
                ans = min(ans, abs(remain - s2[i2 - 1]))
        return ans
