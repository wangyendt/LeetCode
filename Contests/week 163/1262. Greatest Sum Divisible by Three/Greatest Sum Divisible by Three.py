#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Greatest Sum Divisible by Three
@time: 2019/11/19 18:17
"""


class Solution:
    def maxSumDivThree(self, nums: list) -> int:
        res = [0, 0, 0]
        for n in nums:
            for r in res[:]:
                res[(r + n) % 3] = max(res[(r + n) % 3], r + n)
        return res[0]


so = Solution()
print(so.maxSumDivThree([3, 6, 5, 1, 8]))
print(so.maxSumDivThree([4]))
print(so.maxSumDivThree([1, 2, 3, 4, 4]))
