#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/10 23:36
@Author:  wang121ye
@File: Count Triplets That Can Form Two Arrays of Equal XOR.py
@Software: PyCharm
"""

import functools


class Solution:
    def countTriplets(self, arr: list) -> int:
        n = len(arr)
        ret = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                res = functools.reduce(lambda x, y: x ^ y, arr[i:j + 1])
                if res == 0: ret += j - i
        return ret


so = Solution()
print(so.countTriplets(arr=[2, 3, 1, 6, 7]))
print(so.countTriplets(arr=[1, 1, 1, 1, 1]))
print(so.countTriplets(arr=[2, 3]))
print(so.countTriplets(arr=[1, 3, 5, 7, 9]))
print(so.countTriplets(arr=[7, 11, 12, 9, 5, 2, 7, 17, 22]))
