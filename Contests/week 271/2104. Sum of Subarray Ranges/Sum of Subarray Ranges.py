#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of Subarray Ranges.py 
@time: 2021/12/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(arr):
            dp = [0] * n
            right = [i for i in range(n)]
            stack = [0]
            for i in range(1, n, 1):
                curr = arr[i]
                while stack and curr < arr[stack[-1]]:
                    idx = stack.pop()
                    right[idx] = i
                stack.append(i)
            dp[-1] = arr[-1]
            for i in range(n - 2, -1, -1):
                right_idx = right[i]
                if right_idx == i:
                    curr = (n - i) * arr[i]
                    dp[i] = curr
                else:
                    upto_small = (right_idx - i) * (arr[i])
                    curr_sum = (upto_small + dp[right_idx])
                    dp[i] = curr_sum
            return sum(dp)

        return -helper([-num for num in nums]) - helper(nums)


so = Solution()
print(so.subArrayRanges(nums=[1, 2, 3]))
print(so.subArrayRanges(nums=range(1000)))
