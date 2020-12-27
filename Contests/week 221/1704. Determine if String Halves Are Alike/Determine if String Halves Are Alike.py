#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Determine if String Halves Are Alike
@time: 2020/12/27 12:03
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n1 = n2 = 0
        for i in range(len(s)):
            if i < len(s) // 2:
                if s[i] in 'aeiouAEIOU':
                    n1 += 1
            else:
                if s[i] in 'aeiouAEIOU':
                    n2 += 1
        return n1 == n2
