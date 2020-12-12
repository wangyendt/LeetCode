#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Sum of Absolute Differences in a Sorted Array
@time: 2020/12/12 22:33
"""

from typing import *


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        presum = [0]
        postsum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        for num in nums[::-1]:
            postsum.insert(0, postsum[0] + num)
        # print(presum, postsum)
        ret = []
        for i, num in enumerate(nums):
            # print(i, num, presum[i], postsum[i + 1], i * num - presum[i], postsum[i + 1] - (len(nums) - 1 - i) * num)
            ret.append(i * num - presum[i] + postsum[i + 1] - (len(nums) - 1 - i) * num)
        return ret


so = Solution()
print(so.getSumAbsoluteDifferences(nums=[1, 4, 6, 8, 10]))
