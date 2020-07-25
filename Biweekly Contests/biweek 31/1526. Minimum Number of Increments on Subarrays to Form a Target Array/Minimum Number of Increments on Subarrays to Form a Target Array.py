#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Number of Increments on Subarrays to Form a Target Array
@time: 2020/07/26 01:21
"""


class Solution:
    def minNumberOperations(self, target: list) -> int:
        ret = last = 0
        for tar in target:
            ret += max(tar - last, 0)
            last = tar
        return ret


so = Solution()
print(so.minNumberOperations(target=[1, 2, 3, 2, 1]))
print(so.minNumberOperations(target=[3, 1, 1, 2]))
print(so.minNumberOperations(target=[3, 1, 5, 4, 2]))
print(so.minNumberOperations(target=[1, 1, 1, 1]))
