#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: The k Strongest Values in an Array
@time: 2020/06/07 10:34
"""


class Solution:
    def getStrongest(self, arr: list, k: int) -> list:
        n = len(arr)
        arr.sort()
        median_ind = (n - 1) // 2
        mid = arr[median_ind]
        ret = []

        def cmp(a1, a2, m):
            if abs(a1 - m) > abs(a2 - m):
                return True
            elif abs(a1 - m) == abs(a2 - m) and a1 > a2:
                return True
            return False

        for _ in range(k):
            if cmp(arr[0], arr[-1], mid):
                ret.append(arr.pop(0))
            else:
                ret.append(arr.pop())
        return ret


so = Solution()
print(so.getStrongest(arr=[1, 2, 3, 4, 5], k=2))
print(so.getStrongest(arr=[1, 1, 3, 5, 5], k=2))
print(so.getStrongest(arr=[6, 7, 11, 7, 6, 8], k=5))
print(so.getStrongest(arr=[6, -3, 7, 2, 11], k=3))
print(so.getStrongest(arr=[-7, 22, 17, 3], k=2))
