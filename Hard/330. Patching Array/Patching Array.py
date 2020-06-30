#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Patching Array
@time: 2020/06/30 13:52
"""


class Solution:
    def minPatches(self, nums: list, n: int) -> int:
        rgn = 0
        ret = 0
        for num in nums:
            while num > rgn + 1:
                ret += 1
                rgn = 2 * rgn + 1
                if rgn >= n:
                    break
            else:
                rgn += num
                if rgn >= n:
                    break
                continue
            break
        while rgn < n:
            ret += 1
            rgn = 2 * rgn + 1
        return ret


so = Solution()
print(so.minPatches(nums=[1, 3], n=6))
print(so.minPatches(nums=[1, 5, 10], n=20))
print(so.minPatches(nums=[1, 2, 2], n=5))
print(so.minPatches([1, 2, 31, 33], 2147483647))
