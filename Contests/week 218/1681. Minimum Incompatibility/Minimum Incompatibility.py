#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Incompatibility
@time: 2020/12/06 11:01
"""

from typing import *
import itertools
import functools


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        d = len(nums) // k  # the length of each partition

        @functools.lru_cache(None)
        def helper(nums):
            if not nums:
                return 0
            ret = 10 ** 15
            for a in itertools.combinations(nums, d):  # choose a as a partition
                if len(set(a)) < d:  # check for duplicates
                    continue
                left = list(nums)  # numbers left after removing partition a
                for v in a:
                    left.remove(v)
                ret = min(ret, max(a) - min(a) + helper(tuple(left)))
            return ret

        ans = helper(tuple(nums))  # turn the input into a tuple so the function can be cached
        return ans if ans != 10 ** 15 else -1


so = Solution()
# print(so.minimumIncompatibility(nums=[6, 3, 8, 1, 3, 1, 2, 2], k=4))
# print(so.minimumIncompatibility([5, 3, 3, 6, 3, 3], 3))
# print(so.minimumIncompatibility([10, 5, 6, 5, 6, 3, 6, 4, 2, 3], 10))
print(so.minimumIncompatibility([13, 4, 7, 3, 3, 1, 12, 9, 11, 10, 13, 3, 12, 7], 7))
