#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Reverse Subarray To Maximize Array Value
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/27 16:18
@Desc   ：
=================================================="""


class Solution:
    def maxValueAfterReverse(self, nums: list) -> int:
        rgn = max(nums) - min(nums)
        m, M = rgn + 1, -1
        ret, res1 = 0, 0
        for i in range(len(nums) - 1):
            M = max(M, min(nums[i], nums[i + 1]))
            m = min(m, max(nums[i], nums[i + 1]))
            res1 = max(res1, abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1]))
            res1 = max(res1, abs(nums[-1] - nums[i]) - abs(nums[i] - nums[i + 1]))
            ret += abs(nums[i] - nums[i + 1])
        return ret + max(res1, 2 * (M - m))


so = Solution()
print(so.maxValueAfterReverse(nums=[2, 3, 1, 5, 4]))
print(so.maxValueAfterReverse(nums=[2, 4, 9, 24, 2, 1, 10]))
