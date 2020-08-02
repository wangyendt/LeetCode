#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Swaps to Arrange a Binary Grid
@time: 2020/08/03 04:39
"""


class Solution:
    def minSwaps(self, A: list(list())) -> int:
        m, n = len(A), len(A[0])
        res = [0] * m
        for i in range(m):
            for j in range(n):
                if not A[i][~j]:
                    res[i] += 1
                else:
                    break
        ret = 0
        for i, r in enumerate(res):
            target = m - 1 - i
            if res[i] >= target: continue
            for j in range(i + 1, m):
                if res[j] >= target:
                    ret += j - i
                    res[i + 1:j + 1] = res[i:j]
                    break
            else:
                return -1
        return ret


so = Solution()
print(so.minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]))
