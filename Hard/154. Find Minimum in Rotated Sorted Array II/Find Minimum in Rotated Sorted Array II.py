# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/9 17:48
# software: PyCharm

class Solution:
    def findMin(self, nums: list) -> int:
        return min(nums)


so = Solution()
print(so.findMin([1, 3, 5]), 1)
print(so.findMin([2, 2, 2, 0, 1]), 0)
