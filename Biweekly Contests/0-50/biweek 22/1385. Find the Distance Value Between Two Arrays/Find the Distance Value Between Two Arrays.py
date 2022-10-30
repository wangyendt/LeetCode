#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/22 22:50
@Author:  wang121ye
@File: Find the Distance Value Between Two Arrays.py
@Software: PyCharm
"""


class Solution:
    def findTheDistanceValue(self, arr1: list, arr2: list, d: int) -> int:
        arr1.sort()
        arr2.sort()
        i = 0
        j = 0
        dist = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] >= arr2[j]:
                if arr1[i] - arr2[j] > d:
                    j += 1
                else:
                    i += 1
            else:
                if arr2[j] - arr1[i] > d:
                    i += 1
                    dist += 1
                else:
                    i += 1
        dist += len(arr1) - i
        return dist


so = Solution()
print(so.findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))
print(so.findTheDistanceValue(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3))
print(so.findTheDistanceValue(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6))
print(so.findTheDistanceValue([7, 9, 4], [-10], 29))
