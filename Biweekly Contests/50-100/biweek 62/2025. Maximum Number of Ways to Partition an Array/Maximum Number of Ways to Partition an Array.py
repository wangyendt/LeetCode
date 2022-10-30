# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Maximum Number of Ways to Partition an Array.py
@time: 2021/10/02
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *
import collections
import functools
import itertools
import heapq
import pprint


class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = list(itertools.accumulate(nums))
        total_sum = prefix_sums[-1]
        best = 0
        if total_sum % 2 == 0:
            best = prefix_sums[:-1].count(total_sum // 2)

        before_counts = collections.Counter(total_sum - 2 * prefix_sums[p - 1] for p in range(1, n))
        after_counts = collections.Counter()

        best = max(best, before_counts[k - nums[0]])

        for i, x in enumerate(nums[1:]):
            gap = total_sum - 2 * prefix_sums[i]
            before_counts[gap] -= 1
            after_counts[-gap] += 1

            best = max(best, before_counts[k - x] + after_counts[k - x])

        return best


so = Solution()
print(so.waysToPartition(nums=[22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14], k=-33))
print(so.waysToPartition(nums=[0, 0, 0], k=1))
print(so.waysToPartition(nums=[-2, -1, -2], k=3))
print(so.waysToPartition(nums=[2, -1, 2], k=3))
print(so.waysToPartition([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30827, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
print(so.waysToPartition([0, 0, 0, 99, 0, -99, 0], 0))
print(so.waysToPartition([0, 0, 0, 1077, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70590, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1077))
print(so.waysToPartition([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70143, 0, 0], 70143))
