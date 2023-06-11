"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Movement of Robots.py
@time: 20230611
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10 ** 9 + 7
        for i, (num, ss) in enumerate(zip(nums, s)):
            if ss == 'L':
                nums[i] -= d
            else:
                nums[i] += d
        nums.sort()
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0: continue
            dp[i] = (dp[i - 1] + (nums[i] - nums[i - 1]) * i) % MOD
        return sum(dp) % MOD
