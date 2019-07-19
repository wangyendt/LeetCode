# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/19 10:08
# software: PyCharm


import collections


class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        maxQueue = collections.deque()
        ret = []
        for i, n in enumerate(nums):
            while maxQueue and n > nums[maxQueue[-1]]: maxQueue.pop()
            maxQueue.append(i)
            if i - maxQueue[0] >= k: maxQueue.popleft()
            if i >= k - 1: ret.append(nums[maxQueue[0]])
        return ret


so = Solution()
print(so.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(so.maxSlidingWindow([7, 2, 4], 2))
