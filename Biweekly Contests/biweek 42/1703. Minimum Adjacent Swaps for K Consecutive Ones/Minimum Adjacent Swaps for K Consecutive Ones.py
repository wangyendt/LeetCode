#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Adjacent Swaps for K Consecutive Ones
@time: 2020/12/27 00:28
"""

from typing import *


class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        pos = [p for p, x in enumerate(nums) if x == 1]
        # print(pos)

        pos = [p - i for i, p in enumerate(pos)]
        # print(pos)

        mid = k // 2
        sizeleft = mid
        sizeright = k - 1 - sizeleft

        curleft = sum(abs(x - pos[mid]) for x in pos[:sizeleft])
        curright = sum(abs(x - pos[mid]) for x in pos[mid + 1:k])
        minres = curleft + curright

        # print(curleft, curright, minres)

        for ptr in range(1, len(pos) - k + 1):
            # print("ptr", ptr, ptr+mid, ptr+k)
            curleft -= (pos[ptr + mid - 1] - pos[ptr - 1])
            curleft += (pos[ptr + mid] - pos[ptr + mid - 1]) * sizeleft

            curright -= (pos[ptr + mid] - pos[ptr + mid - 1]) * sizeright
            curright += (pos[ptr + k - 1] - pos[ptr + mid])

            minres = min(minres, curleft + curright)
            # print(curleft, curright, minres)

        # print()
        return minres
