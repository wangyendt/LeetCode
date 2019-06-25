# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/25 2:05
# software: PyCharm

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, mountain):
        self.mountain = mountain

    def get(self, index: int) -> int:
        return self.mountain[index]

    def length(self) -> int:
        return len(self.mountain)


class Solution:
    def findInMountainArray(self, mountain_arr: 'MountainArray', target: int) -> int:
        n = len(mountain_arr)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if mountain_arr[m] < mountain_arr[m + 1]:
                l = m + 1
            else:
                r = m
        peak = l
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            if mountain_arr[m] < target:
                l = m + 1
            elif mountain_arr[m] > target:
                r = m - 1
            else:
                return m
        l, r = peak, n - 1
        while l <= r:
            m = (l + r) // 2
            if mountain_arr[m] > target:
                l = m + 1
            elif mountain_arr[m] < target:
                r = m - 1
            else:
                return m
        return -1


ma = MountainArray()
so = Solution()
# print(so.findInMountainArray(3, ma), 2)
print(so.findInMountainArray([1, 2, 3, 4, 5, 3, 1], 3), 2)
