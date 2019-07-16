# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 15:12
# software: PyCharm
import collections


class Solution:
    def findPairs(self, nums: list, k: int) -> int:
        if not nums or k < 0: return 0
        if k == 0:
            return len([c[0] for c in collections.Counter(nums).items() if c[1] > 1])
        ret = 0
        nums = set(nums)
        for n in nums:
            if n + k in nums:
                ret += 1
        return ret


so = Solution()
print(so.findPairs([1, 3, 1, 5, 4], 0))
