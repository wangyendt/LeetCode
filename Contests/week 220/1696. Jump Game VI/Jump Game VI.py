#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Jump Game VI
@time: 2020/12/20 10:49
"""

from typing import *
import collections


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        '''
            clearly it is a DP problem. dp[i] represents the max Score if you are at that idx
            nums = [1,-1,-2,4,-7,3], k = 2
            dp   = [1,0,-1,4,-3,7]

                    dp[i] = max(nums[i] + dp[i-2], nums[i] + dp[i-2+1])
                there will be k combos to find the max of ^^^
                -so since all of those combos will add nums[i]
                basically we just need to find the max DP                                                                                                   in the range of [i-k, i] inclusive, and dp[i] will equal nums[i] + maxDPVal in the range from i-k to i

            -hmmm so how do we keep track of that max in each window of length k
            -might need to do a sliding window max algorithm wih deque
                -the deque's first element will ALWAYS hold the maxValue of the k DPs before idx i


            nums = [10,-5,-2,4,0,3], k = 3
            dp   = [10,5,8,14,14,17]

           deque = [(10,0)(5,1)]



        '''

        dp = [0] * len(nums)
        dp[0] = nums[0]
        d = collections.deque([(nums[0], 0)])
        for i in range(1, len(nums)):
            dp[i] = nums[i] + d[0][0]

            while d and d[-1][0] < dp[i]:  # sliding window maximum variation
                d.pop()  # sliding window maximum variation
            d.append((dp[i], i))  # sliding window maximum variation

            if i - k == d[0][1]:  # sliding window maximum variation
                d.popleft()  # sliding window maximum variation

        return dp[-1]


so = Solution()
print(so.maxResult(nums=[1, -1, -2, 4, -7, 3], k=2))
print(so.maxResult(nums=[10, -5, -2, 4, 0, 3], k=3))
# print(so.maxResult(nums=list(range(10000)), k=10000))
