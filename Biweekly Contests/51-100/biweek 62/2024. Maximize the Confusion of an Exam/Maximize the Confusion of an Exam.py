# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Maximize the Confusion of an Exam.py
@time: 2021/10/02
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *
import collections
import functools
import itertools


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        A = answerKey
        n = len(A)
        nt = sum(1 for a in A if a == 'T')
        nf = n - nt
        if k >= min(nt, nf):
            return n

        def helper(arr: str, ch='F'):
            arr = ch + arr + ch
            stack = []
            cnt = 0
            ret = 0
            for i, a in enumerate(arr):
                if a == ch:
                    stack.append(i)
                    cnt += 1
                if cnt >= k + 2:
                    ret = max(ret, stack[-1] - stack[0] - 1)
                    cnt -= 1
                    stack.pop(0)
            return ret

        return max(helper(A, 'F'), helper(A, 'T'))


so = Solution()
print(so.maxConsecutiveAnswers(answerKey="TTFF", k=2))
print(so.maxConsecutiveAnswers(answerKey="TFFT", k=1))
print(so.maxConsecutiveAnswers(answerKey="TTFTTFTT", k=1))
print(so.maxConsecutiveAnswers(answerKey="TFTTTFFTTTTFTTTFTTT", k=2))
