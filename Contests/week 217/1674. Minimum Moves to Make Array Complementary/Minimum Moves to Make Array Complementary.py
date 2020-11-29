#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Moves to Make Array Complementary
@time: 2020/11/29 11:17
"""

from typing import *


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        move0 = [0] * (limit * 2 + 2)
        move1 = [0] * (limit * 2 + 2)

        for i in range(len(nums) // 2):
            a, b = nums[i], nums[len(nums) - 1 - i]
            a, b = min(a, b), max(a, b)

            move0[a + b] += 1

            # note a + 1 <= b + 1 <= a + b <= a + limit <= b + limit
            # making one change, we take all values from a+1 to b+limit
            # but we make no change if total is a+b

            sm, lg = a + 1, b + limit
            move1[sm] += 1
            move1[a + b] -= 1
            move1[a + b + 1] += 1
            move1[lg + 1] -= 1

        # now iterate and calculate the number of moves and find the smallest
        res = len(nums)

        ps = 0
        for i in range(len(move0)):
            ps += move1[i]  # use partial sum to record the number of pairs that can take 1 move when the target is i
            # number of elements - ones that take 0 move - ones that takes 1 move
            res = min(res, len(nums) - 2 * move0[i] - ps)
        return res


so = Solution()
print(so.minMoves(nums=[1, 2, 4, 3], limit=4))
print(so.minMoves(nums=[1, 2, 2, 1], limit=2))
print(so.minMoves(nums=[1, 2, 1, 2], limit=2))
