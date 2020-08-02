#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count Good Triplets
@time: 2020/08/03 03:45
"""


class Solution:
    def countGoodTriplets(self, arr: list, a: int, b: int, c: int) -> int:
        n = len(arr)
        ret = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[k] - arr[i]) <= c:
                        ret += 1
        return ret
