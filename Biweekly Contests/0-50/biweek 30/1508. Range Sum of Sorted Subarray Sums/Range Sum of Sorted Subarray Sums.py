#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Range Sum of Sorted Subarray Sums
@time: 2020/07/11 22:34
"""


class Solution:
    def rangeSum(self, nums: list, n: int, left: int, right: int) -> int:
        res = []
        for l in range(1, n + 1):
            i = 0
            while i + l <= n:
                res.append(sum(nums[i:i + l]))
                i += 1
        res.sort()
        return sum(res[left - 1:right]) % (10 ** 9 + 7)


so = Solution()
print(so.rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=5))
