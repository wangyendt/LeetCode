#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Arithmetic Subarrays
@time: 2020/10/25 10:37
"""

from typing import *


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr: List[int]) -> bool:
            if len(arr) == 2: return True
            arr.sort()
            if all([arr[i + 1] - arr[i] == arr[1] - arr[0] for i in range(len(arr) - 1)]):
                return True
            return False

        n = len(nums)
        m = len(l)
        ret = []
        for i in range(m):
            arr = nums[l[i]:r[i] + 1].copy()
            ret.append(check(arr))
        return ret


so = Solution()
print(so.checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))
