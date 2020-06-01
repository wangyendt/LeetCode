#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Burst Balloons
@time: 2020/05/26 09:48
"""

import functools
import sys


class Solution:
    def maxCoins(self, nums: list) -> int:
        nums = [1] + nums + [1]

        @functools.lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            elif i == j:
                return nums[i] * nums[i - 1] * nums[i + 1]
            else:
                return max(nums[i - 1] * nums[k] * nums[j + 1] + dp(i, k - 1) + dp(k + 1, j) for k in range(i, j + 1))

        return dp(1, len(nums) - 2)


so = Solution()
# print(so.maxCoins([3, 1, 5, 8]))
print(so.maxCoins([8, 3, 4, 3, 5, 0, 5, 6, 6, 2, 8, 5, 6, 2, 3, 8, 3, 5, 1, 0, 2]))
