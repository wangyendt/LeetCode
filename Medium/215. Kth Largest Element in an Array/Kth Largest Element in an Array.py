#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Kth Largest Element in an Array.py 
@time: 2019/09/04
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import heapq


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        def helper(arr, _k):
            buffer = []
            for n in arr:
                heapq.heappush(buffer, n)
                if len(buffer) > _k:
                    heapq.heappop(buffer)
            return min(buffer)

        if 2 * k <= len(nums):
            return helper(nums, k)
        else:
            return -helper([-n for n in nums], len(nums) + 1 - k)


so = Solution()
for i in range(1, 7):
    print(i, so.findKthLargest([3, 2, 1, 5, 6, 4], i))
