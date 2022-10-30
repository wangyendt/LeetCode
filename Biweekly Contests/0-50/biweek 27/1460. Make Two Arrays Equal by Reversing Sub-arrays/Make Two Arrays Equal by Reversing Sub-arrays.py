#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Make Two Arrays Equal by Reversing Sub-arrays
@time: 2020/05/30 22:31
"""

import collections


class Solution:
    def canBeEqual(self, target: list, arr: list) -> bool:
        return collections.Counter(target) == collections.Counter(arr)


so = Solution()
print(so.canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))
print(so.canBeEqual(target=[7], arr=[7]))
print(so.canBeEqual(target=[1, 12], arr=[12, 1]))
print(so.canBeEqual(target=[3, 7, 9], arr=[3, 7, 11]))
print(so.canBeEqual(target=[1, 1, 1, 1, 1], arr=[1, 1, 1, 1, 1]))
