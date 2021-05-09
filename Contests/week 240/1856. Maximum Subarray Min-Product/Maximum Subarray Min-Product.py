#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Subarray Min-Product.py 
@time: 2021/05/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import sys

sys.setrecursionlimit(1000000)


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left_bound = [0] * n  # left_bound[i] stores index of farthest element greater or equal to nums[i]
        right_bound = [0] * n  # right_bound[i] stores index of farthest element greater or equal to nums[i]
        st = []
        for i in range(0, n):
            while st and nums[st[-1]] >= nums[i]: st.pop()
            if len(st) > 0:
                left_bound[i] = st[-1] + 1
            else:
                left_bound[i] = 0
            st.append(i)

        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] >= nums[i]: st.pop()
            if len(st) > 0:
                right_bound[i] = st[-1] - 1
            else:
                right_bound[i] = n - 1
            st.append(i)

        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]

        def getSum(left, right):  # inclusive
            return preSum[right + 1] - preSum[left]

        maxProduct = 0
        for i in range(n):
            maxProduct = max(maxProduct, nums[i] * getSum(left_bound[i], right_bound[i]))

        return maxProduct % (10 ** 9 + 7)


so = Solution()
print(so.maxSumMinProduct([1, 2, 3, 2]))
print(so.maxSumMinProduct(list(range(100000))))
