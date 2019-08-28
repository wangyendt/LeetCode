# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/28 10:41
# software: PyCharm

import sys


class Solution:
    def minSubArrayLen(self, s: int, nums: list) -> int:
        sum_, ret, length, stack = 0, sys.maxsize, 0, []
        if sum(nums) < s: return 0
        for n in nums:
            length += 1
            sum_ += n
            stack.append(n)
            while sum_ >= s:
                ret = min(ret, length)
                sum_ -= stack.pop(0)
                length -= 1
        return ret


so = Solution()
print(so.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(so.minSubArrayLen(7, []))
