# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/12 11:40
# software: PyCharm

class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        if not nums: return []
        M = len(nums)
        nums = set(nums)
        return list(set(range(1, M + 1)) - nums)


so = Solution()
print(so.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(so.findDisappearedNumbers([1, 1]))
