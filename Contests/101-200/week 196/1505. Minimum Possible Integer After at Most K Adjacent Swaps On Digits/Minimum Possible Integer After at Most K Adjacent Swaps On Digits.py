#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Possible Integer After at Most K Adjacent Swaps On Digits
@time: 2020/07/05 10:58
"""


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        # greedy O(n^2)
        n = len(num)
        arr = list(map(int, num))
        if k >= n * (n - 1): return ''.join(sorted(num))
        for i in range(n - 1):
            pos = i
            for j in range(i + 1, n):
                if j - i > k:
                    break
                if arr[j] < arr[pos]:
                    pos = j
            for j in range(pos, i, -1):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            k -= pos - i
        return ''.join(map(str, arr))


so = Solution()
print(so.minInteger(num="4321", k=4))
print(so.minInteger(num="100", k=1))
print(so.minInteger(num="36789", k=1000))
print(so.minInteger(num="22", k=22))
print(so.minInteger(num="9438957234785635408", k=23))
