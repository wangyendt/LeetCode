#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/2/21 19:14
@Desc   ：
=================================================="""


class Solution:
    def numOfSubarrays(self, arr: list, k: int, threshold: int) -> int:
        ret = 0
        n = len(arr)
        sum_ = 0
        target = k * threshold
        for i in range(n):
            sum_ += arr[i]
            if i > k - 2:
                if sum_ >= target: ret += 1
                sum_ -= arr[i - k + 1]
        return ret


so = Solution()
print(so.numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))
print(so.numOfSubarrays(arr=[1, 1, 1, 1, 1], k=1, threshold=0))
print(so.numOfSubarrays(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5))
print(so.numOfSubarrays(arr=[7, 7, 7, 7, 7, 7, 7], k=7, threshold=7))
print(so.numOfSubarrays(arr=[4, 4, 4, 4], k=4, threshold=1))
