#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Decompress Run-Length Encoded List
@time: 2020/1/15 14:18
"""


class Solution:
    def decompressRLElist(self, nums: list) -> list:
        n = len(nums)
        ret = []
        for i in range(0, n, 2):
            ret += [nums[i + 1]] * nums[i]
        return ret


so = Solution()
print(so.decompressRLElist([1, 2, 3, 4]))
print(so.decompressRLElist([1, 2, 3, 4, 5, 6]))
