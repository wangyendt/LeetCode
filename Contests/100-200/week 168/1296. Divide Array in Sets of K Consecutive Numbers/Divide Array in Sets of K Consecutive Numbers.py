#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Divide Array in Sets of K Consecutive Numbers
@time: 2019/12/24 10:43
"""

import collections


class Solution:
    def isPossibleDivide(self, nums: list, k: int) -> bool:
        if len(nums) % k != 0: return False
        cnter = collections.Counter(nums)
        while cnter:
            m = min(cnter)
            for i in range(k):
                if m + i in cnter:
                    cnter[m + i] -= 1
                    if cnter[m + i] == 0:
                        cnter.pop(m + i)
                else:
                    return False
        return True


so = Solution()
print(so.isPossibleDivide(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4))
print(so.isPossibleDivide(nums=[3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], k=3))
print(so.isPossibleDivide(nums=[3, 3, 2, 2, 1, 1], k=3))
print(so.isPossibleDivide(nums=[1, 2, 3, 4], k=3))
