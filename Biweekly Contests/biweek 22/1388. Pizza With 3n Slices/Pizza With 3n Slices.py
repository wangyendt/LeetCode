#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/23 0:24
@Author:  wang121ye
@File: Pizza With 3n Slices.py
@Software: PyCharm
"""

import functools


class Solution:
    def maxSizeSlices(self, A: list):
        @functools.lru_cache(None)
        def dp(i, j, k, cycle=0):
            # i,j = start,end (inclusive)
            # k = remaining
            # cycle (see comment on cycle variable)

            if k == 1:
                # one remaining, calculate immediately
                return max(A[i:j + 1])

            if j - i + 1 < k * 2 - 1:
                # not possible because not enough elements remain
                return -float('inf')

            return max(A[j] +  # take last element
                       dp(i + cycle, j - 2,  # dp on i to j-2
                          k - 1),  # one less element left to take
                       # (on the cycle variable)
                       # if the last element of the inital array is taken
                       # you cannot take the first element of the inital array
                       # Alternatively, you choose not to take element j
                       dp(i, j - 1,  # dp on i to j-1
                          k))  # same number of elements to take

        return dp(0, len(A) - 1,  # dp on 0 to length-1
                  len(A) // 3,  # number of elements to take
                  1)  # see comment on cycle variable

        # lru_cache to reduce search space


so = Solution()
print(so.maxSizeSlices(A=[1, 2, 3, 4, 5, 6]))
print(so.maxSizeSlices(A=[8, 9, 8, 6, 1, 1]))
print(so.maxSizeSlices(A=[4, 1, 2, 5, 8, 3, 1, 9, 7]))
print(so.maxSizeSlices(A=[3, 1, 2]))
