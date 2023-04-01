#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
@time: 2020/08/09 18:38
"""

import collections
import bisect
import functools


class Solution:
    def maxNonOverlapping(self, nums: list, target: int) -> int:
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)
        n = len(nums)
        mems = {0: 0}
        ret = 0
        for i in range(1, n + 1):
            cur = pre[i]
            prev = cur - target
            if prev in mems:
                ret += 1
                mems.clear()
            mems[cur] = i
        return ret


so = Solution()
print(so.maxNonOverlapping(nums=[1, 1, 1, 1, 1], target=2))
print(so.maxNonOverlapping(nums=[-1, 3, 5, 1, 4, 2, -9], target=6))
print(so.maxNonOverlapping(nums=[-2, 6, 6, 3, 5, 4, 1, 2, 8], target=10))
print(so.maxNonOverlapping(nums=[0, 0, 0], target=0))
