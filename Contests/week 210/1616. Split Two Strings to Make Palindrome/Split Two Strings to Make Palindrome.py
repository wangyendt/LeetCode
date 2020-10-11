#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Split Two Strings to Make Palindrome
@time: 2020/10/11 12:04
"""


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        if n == 1: return True
        for i in range(n):
            if i > n // 2 or a[i] != b[~i]:
                break
        i1 = i
        for i in range(n):
            if i > n // 2 or a[~i] != b[i]:
                break
        i2 = i
        r1 = r2 = 0
        i_start = (n - 1) // 2
        for i in range(i_start):
            if a[i_start - i] == a[~(i_start - i)]:
                r1 += 2
                if i_start - i == ~(i_start - i):
                    r1 -= 1
            else:
                break
        for i in range(i_start):
            if b[i_start - i] == b[~(i_start - i)]:
                r2 += 2
                if i_start - i == ~(i_start - i):
                    r2 -= 1
            else:
                break
        return 2 * max(i1, i2) + max(r1, r2) >= n
