"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Maximum Number of Marked Indices.py
@time: 20230627
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        m = len(nums) // 2
        i, j = 0, m
        res = 0
        nums.sort()
        while i < m and j < len(nums):
            if nums[j] >= nums[i] * 2:
                res += 2
                i += 1
            j += 1
        return res


so = Solution()
print(so.maxNumOfMarkedIndices(nums=[9, 2, 5, 4]))
print(so.maxNumOfMarkedIndices([1, 78, 27, 48, 14, 86, 79, 68, 77, 20, 57, 21, 18, 67, 5, 51, 70, 85, 47, 56, 22, 79, 41, 8, 39, 81, 59, 74, 14, 45, 49, 15, 10, 28, 16, 77, 22, 65, 8, 36, 79, 94, 44, 80, 72, 8, 96, 78, 39, 92, 69, 55, 9, 44, 26, 76, 40, 77, 16, 69, 40, 64, 12, 48, 66, 7, 59, 10]))
