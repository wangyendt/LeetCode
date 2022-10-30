#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Sub-arrays With Odd Sum
@time: 2020/07/26 00:38
"""


class Solution:
    def numOfSubarrays(self, arr: list) -> int:
        for i in range(len(arr)):
            if i > 0:
                arr[i] += arr[i - 1]
        arr = [0] + arr
        ret = 0
        cnt = [0, 0]  # odd,even
        for a in arr:
            if a % 2:
                cnt[0] += 1
                ret += cnt[1]
            else:
                cnt[1] += 1
                ret += cnt[0]
        return ret % (10 ** 9 + 7)


so = Solution()
print(so.numOfSubarrays([1, 3, 5]))
print(so.numOfSubarrays([2, 4, 6]))
print(so.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))
print(so.numOfSubarrays([100, 100, 99, 99]))
print(so.numOfSubarrays([7]))
