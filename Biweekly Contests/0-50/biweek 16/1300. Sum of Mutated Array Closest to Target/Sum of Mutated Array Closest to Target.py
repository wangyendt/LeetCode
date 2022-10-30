#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Sum of Mutated Array Closest to Target
@time: 2020/1/3 14:06
"""


class Solution:
    def findBestValue(self, arr: list, target: int) -> int:
        n = len(arr)
        left_sum = 0
        arr.sort()
        p = 0
        for i in range(n):
            p = i
            if target - left_sum <= arr[i] * (n - i):
                break
            left_sum += arr[i]
        res = (target - left_sum) / (n - p)
        return int(res) if res - int(res) <= 0.5 else int(res) + 1


so = Solution()
print(so.findBestValue(arr=[4, 9, 3], target=10))
print(so.findBestValue(arr=[2, 3, 5], target=10))
print(so.findBestValue(arr=[60864, 25176, 27249, 21296, 20204], target=56803))
