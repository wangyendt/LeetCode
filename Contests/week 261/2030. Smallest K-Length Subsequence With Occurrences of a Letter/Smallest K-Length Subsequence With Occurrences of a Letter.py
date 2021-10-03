# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Smallest K-Length Subsequence With Occurrences of a Letter.py
@time: 2021/10/04
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

import itertools


class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        l, r = letter, repetition
        n, stack = len(s), ["!"]
        suff = list(itertools.accumulate([c == l for c in s][::-1]))[::-1]

        for i, c in enumerate(s):
            while stack[-1] > c and len(stack) + n - i > k + 1 and (stack[-1] != l or r < suff[i]):
                r += stack.pop() == l
            if len(stack) < min(k, k - r + (c == l)) + 1:
                stack += [c]
                r -= (c == l)

        return "".join(stack[1:])
