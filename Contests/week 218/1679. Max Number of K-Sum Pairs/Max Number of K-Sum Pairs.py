#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Max Number of K-Sum Pairs
@time: 2020/12/06 10:33
"""

from typing import *
import collections


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnter = collections.Counter([n for n in nums])
        ret = 0
        for n in nums:
            # print(n, k - n, cnter, end=' ')
            if k - n in cnter and cnter[k - n] > 0 and cnter[n] > 0:
                if n == k - n and cnter[k - n] < 2:
                    continue
                cnter[n] -= 1
                cnter[k - n] -= 1
                ret += 1
            # print(ret)
        return ret


so = Solution()
# print(so.maxOperations([3, 1, 3, 4, 3], 6))
print(so.maxOperations([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3))
