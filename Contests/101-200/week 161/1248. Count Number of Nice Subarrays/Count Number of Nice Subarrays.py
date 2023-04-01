#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count Number of Nice Subarrays
@time: 2019/11/8 14:33
"""


class Solution:
    def numberOfSubarrays(self, A: list, k: int) -> int:
        def atMost(k):
            res = i = 0
            for j in range(len(A)):
                k -= A[j] % 2
                while k < 0:
                    k += A[i] % 2
                    i += 1
                res += j - i + 1
            return res

        return atMost(k) - atMost(k - 1)
