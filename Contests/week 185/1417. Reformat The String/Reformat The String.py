#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/19 10:31
@Author:  wang121ye
@File: Reformat The String.py
@Software: PyCharm
"""


class Solution:
    def reformat(self, s: str) -> str:
        digits, letters = [], []
        for t in s:
            if str(t).isdigit():
                digits.append(t)
            else:
                letters.append(t)
        m, n = len(digits), len(letters)
        if abs(m - n) > 1:
            return ''
        ret = ''
        if m < n:
            A, B = letters, digits
        else:
            A, B = digits, letters
        for i in range(min(len(A), len(B))):
            ret = ret + A[i] + B[i]
        if m != n:
            ret = ret + A[-1]
        return ret


so = Solution()
print(so.reformat(s="a0b1c2"))
print(so.reformat(s="leetcode"))
print(so.reformat(s="1229857369"))
print(so.reformat(s="covid2019"))
print(so.reformat(s="ab123"))
