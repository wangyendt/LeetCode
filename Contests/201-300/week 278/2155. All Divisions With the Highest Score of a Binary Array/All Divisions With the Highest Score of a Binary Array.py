#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: All Divisions With the Highest Score of a Binary Array
@time: 2022/02/01 01:52
"""

from typing import *
import collections


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeroFromLeft = [0] * (len(nums) + 1)
        oneFromRight = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroFromLeft[i + 1] = zeroFromLeft[i] + 1
            else:
                zeroFromLeft[i + 1] = zeroFromLeft[i]

        for i in range(len(nums))[::-1]:
            if nums[i] == 1:
                oneFromRight[i] = oneFromRight[i + 1] + 1
            else:
                oneFromRight[i] = oneFromRight[i + 1]

        allSum = [0] * (len(nums) + 1)
        currentMax = 0
        res = []
        for i in range(len(nums) + 1):
            allSum[i] = oneFromRight[i] + zeroFromLeft[i]
            if allSum[i] > currentMax:
                res = []
                currentMax = allSum[i]
            if allSum[i] == currentMax:
                res.append(i)
        return res


so = Solution()
print(so.maxScoreIndices(nums=[0, 0, 1, 0]))
