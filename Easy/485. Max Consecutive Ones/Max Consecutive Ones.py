# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/12 18:16
# software: PyCharm


class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        start, end = 0, 0
        ret = 0
        if len(nums) == 1: return 1 if nums[0] == 1 else 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                start = i + 1
            elif nums[i + 1] - nums[i] == -1:
                end = i
                ret = max(ret, end - start + 1)
        return ret


so = Solution()
print(so.findMaxConsecutiveOnes([0, 1, 1, 1, 1, 0, 1, 1, 1]), 4)
