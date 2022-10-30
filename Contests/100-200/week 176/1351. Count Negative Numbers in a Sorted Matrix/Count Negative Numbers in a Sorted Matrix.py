#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count Negative Numbers in a Sorted Matrix
@time: 2020/2/26 14:08
"""


class Solution:
    def countNegatives(self, A: list(list())) -> int:
        m, n = len(A), len(A[0])

        def count_negative_one_row(row, r0=n - 1):
            l, r = 0, r0
            while l < r:
                m = (l + r + 1) // 2
                if row[m] >= 0:
                    l = m
                else:
                    r = m - 1
            return l  # l+n-2

        ret = 0
        r_last = n - 1
        for i, a in enumerate(A):
            r_last = count_negative_one_row(a, r_last)
            # print(f'rlast:{r_last}')
            if a[0] < 0:
                ret += n
            else:
                ret += n - 1 - r_last
        return ret


so = Solution()
print(so.countNegatives(A=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(so.countNegatives(A=[[3, 2], [1, 0]]))
print(so.countNegatives(A=[[1, -1], [-1, -1]]))
print(so.countNegatives(A=[[-1]]))
