#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Construct Target Array With Multiple Sums
@time: 2020/2/26 16:03
"""

import heapq


class Solution:
    def isPossible(self, target: list) -> bool:
        total = sum(target)
        A = [-a for a in target]
        heapq.heapify(A)
        while True:
            a = -heapq.heappop(A)
            total -= a
            if a == 1 or total == 1: return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(A, -a)


so = Solution()
print(so.isPossible(target=[9, 3, 5]))
print(so.isPossible(target=[1, 1, 1, 2]))
print(so.isPossible(target=[8, 5]))
