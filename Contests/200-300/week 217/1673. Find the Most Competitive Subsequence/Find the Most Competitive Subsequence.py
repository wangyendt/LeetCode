#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find the Most Competitive Subsequence
@time: 2020/11/29 10:43
"""

from typing import *
import heapq
import bisect


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ret = []
        for i, n in enumerate(nums):
            ret.append(n)
            # print(ret)
            while True:
                if len(ret) >= 2 and ret[-1] < ret[-2]:
                    if len(ret) + len(nums) - i - 1 > k:
                        ret.pop(len(ret) - 2)
                    else:
                        break
                else:
                    break
        return ret[:k]


so = Solution()
print(so.mostCompetitive([3, 5, 2, 6], 2))
# print(so.mostCompetitive(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4))
