# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/9 17:57
# software: PyCharm


class Solution:
    def maximumGap(self, nums: list) -> int:
        def radixSort(A):
            for k in range(10):
                s = [[] for i in range(10)]
                for i in A:
                    s[i // (10 ** k) % 10].append(i)
                A = [a for b in s for a in b]
            return A

        A = radixSort(nums)
        ans = 0
        if len(A) == 0:
            return 0
        prev = A[0]
        for i in A:
            if i - prev > ans: ans = i - prev
            prev = i
        return ans
