#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Absolute Sum Difference
@time: 2021/04/04 10:44
"""

from typing import *
import bisect


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        ret = 0
        M = 0
        for n1, n2 in zip(nums1, nums2):
            ret += abs(n1 - n2)
            M = max(M, abs(n1 - n2))
        if M == 0:
            return ret
        s = ret
        M = 0
        h = []
        indices = sorted(list(range(len(nums1))), key=lambda x: abs(nums1[x] - nums2[x]))
        n11, n22 = [nums1[ind] for ind in indices], [nums2[ind] for ind in indices]
        nums1, nums2 = n11, n22
        for n1, n2 in zip(nums1, nums2):
            tmp = abs(n1 - n2)
            if tmp >= M:
                M = tmp
                idx = bisect.bisect(h, n2)
                res = tmp
                for i in (idx - 1, idx, idx + 1):
                    if 0 <= i < len(h):
                        res = min(res, abs(h[i] - n2))
                ret = min(ret, s + res - tmp)
            j = bisect.bisect(h, n1)
            h[j:j] = [n1]
        return ret % (10 ** 9 + 7)


so = Solution()
print(so.minAbsoluteSumDiff(nums1=[1, 10, 4, 4, 2, 7], nums2=[9, 3, 5, 1, 7, 4]))
print(so.minAbsoluteSumDiff(
    [53, 48, 14, 71, 31, 55, 6, 80, 28, 19, 15, 40, 7, 21, 69, 15, 5, 42, 86, 15, 11, 54, 44, 62, 9, 100, 2, 26, 81, 87,
     87, 18, 45, 29, 46, 100, 20, 87, 49, 86, 14, 74, 74, 52, 52, 60, 8, 25, 21, 96, 7, 90, 91, 42, 32, 34, 55, 20, 66,
     36, 64, 67, 44, 51, 4, 46, 25, 57, 84, 23, 10, 84, 99, 33, 51, 28, 59, 88, 50, 41, 59, 69, 59, 65, 78, 50, 78, 50,
     39, 91, 44, 78, 90, 83, 55, 5, 74, 96, 77, 46],
    [39, 49, 64, 34, 80, 26, 44, 3, 92, 46, 27, 88, 73, 55, 66, 10, 4, 72, 19, 37, 40, 49, 40, 58, 82, 32, 36, 91, 62,
     21, 68, 65, 66, 55, 44, 24, 78, 56, 12, 79, 38, 53, 36, 90, 40, 73, 92, 14, 73, 89, 28, 53, 52, 46, 84, 47, 51, 31,
     53, 22, 24, 14, 83, 75, 97, 87, 66, 42, 45, 98, 29, 82, 41, 36, 57, 95, 100, 2, 71, 34, 43, 50, 66, 52, 6, 43, 94,
     71, 93, 61, 28, 84, 7, 79, 23, 48, 39, 27, 48, 79]))
