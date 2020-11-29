#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimize Deviation in Array
@time: 2020/11/29 11:39
"""

from typing import *

import heapq


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []

        # record the lower and upper bound for each number
        for i, n in enumerate(nums):
            if n % 2 == 0:
                maxx = n
                while n % 2 == 0:
                    n //= 2
                pq.append([n, maxx])
            else:
                pq.append([n, n * 2])

        # determine the miminum upper bound for each even number
        maxx = max([val[0] for val in pq])

        heapq.heapify(pq)

        res = maxx - pq[0][0]

        while True:
            val, bound = heapq.heappop(pq)
            if val >= bound:
                break
            maxx = max(val * 2, maxx)
            heapq.heappush(pq, [val * 2, bound])

            res = min(res, maxx - pq[0][0])

        return res


so = Solution()
# print(so.minimumDeviation([1, 2, 3, 4]))
print(so.minimumDeviation([3, 5]))
print(so.minimumDeviation([10, 4, 3]))
