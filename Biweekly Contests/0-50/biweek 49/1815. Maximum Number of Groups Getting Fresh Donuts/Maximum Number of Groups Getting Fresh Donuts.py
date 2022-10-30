#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: 4
@time: 2021/04/03 22:29
"""

from typing import *
import collections


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        N = len(groups)

        # We only need to worry about the non-zero remainder
        groups = [i % batchSize for i in groups if i % batchSize]

        # Can already satisfied
        satisfied = N - len(groups)

        # For those groups that complement each other, we can only satisfy one group
        matching = collections.defaultdict(int)
        for group in groups:
            if matching[batchSize - group] > 0:
                matching[batchSize - group] -= 1
                satisfied += 1
            else:
                matching[group] += 1

        groups = []
        for group, count in matching.items():
            groups += [group] * count

        cache = dict()

        # Brute force the rest
        def allocate(leftOver: int, groups: list) -> int:
            if not groups:
                return 0

            key = (leftOver, tuple(groups))
            if key in cache:
                return cache[key]

            result = 0
            for i in range(len(groups)):
                nextGroups = groups[0: i] + groups[i + 1:]
                nextLeftOver = leftOver - groups[i]
                while nextLeftOver < 0:
                    nextLeftOver += batchSize
                result = max(result, allocate(nextLeftOver, nextGroups))

            result += int(leftOver == 0)
            cache[key] = result
            return result

        return allocate(0, groups) + satisfied


so = Solution()
print(so.maxHappyGroups(batchSize=3, groups=[1, 2, 3, 4, 5, 6, 2, 4, 1, 1, 2, 3, 4, 1, 1, 2, 3, 3, 1, 1, 4, 5, 6, 3]))
