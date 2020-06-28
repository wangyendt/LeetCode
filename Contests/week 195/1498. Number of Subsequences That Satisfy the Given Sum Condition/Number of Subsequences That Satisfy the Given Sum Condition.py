#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Subsequences That Satisfy the Given Sum Condition
@time: 2020/06/28 11:15
"""

import bisect
import collections


class Solution:
    def numSubseq(self, nums: list, target: int) -> int:
        ret = 0
        modulo = 10 ** 9 + 7
        nums.sort()
        power = collections.defaultdict(int)
        for i, n in enumerate(nums):
            if n * 2 > target:
                break
            else:
                ind = bisect.bisect_right(nums, target - n, lo=i)
                # print(i, n, ind)
                if i < ind:
                    if ind - i - 1 in power:
                        res = power[ind - i - 1]
                    else:
                        res = 2 ** (ind - i - 1)
                        power[ind - i - 1] = res % modulo
                    ret += res
        return ret % modulo


so = Solution()
# print(so.numSubseq(nums=[3, 3, 3, 3, 6], target=2))
# print(so.numSubseq(nums=[3, 4, 5, 6, 8], target=3))
# print(so.numSubseq(nums=[3, 3, 3, 3, 6], target=4))
# print(so.numSubseq(nums=[3, 3, 3, 3, 6], target=6))
# print(so.numSubseq(nums=[3, 4, 6, 7, 8], target=6))
# print(so.numSubseq(nums=[3, 3, 3, 4, 6], target=7))
# print(so.numSubseq(nums=[3, 3, 3, 4, 6], target=8))
print(so.numSubseq(nums=[3, 5, 6, 7], target=9))
print(so.numSubseq(nums=[3, 3, 6, 8], target=10))
print(so.numSubseq(nums=[2, 3, 3, 4, 6, 7], target=12))
print(so.numSubseq(nums=[5, 2, 4, 1, 7, 6, 8], target=16))
