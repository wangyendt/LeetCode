# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/12 11:48
# software: PyCharm

class Solution:
    def minMoves(self, nums: list) -> int:
        # sum(x) + (n-1)*h = n*(min + h)
        return sum(nums) - min(nums) * len(nums)


so = Solution()
print(so.minMoves([1, 2, 3]))
