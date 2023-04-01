# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: The Score of Students Solving Math Expression.py
@time: 2021/09/26
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *
import functools


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        op = ""
        stack = []
        for ch in s:
            if ch in "+*":
                op = ch
            else:
                x = int(ch)
                if op == "*":
                    stack[-1] *= x
                else:
                    stack.append(x)
        target = sum(stack)

        @functools.lru_cache(None)
        def fn(lo, hi):
            """Return possible answers of s[lo:hi]."""
            if lo + 1 == hi: return {int(s[lo])}
            ans = set()
            for mid in range(lo + 1, hi, 2):
                for x in fn(lo, mid):
                    for y in fn(mid + 1, hi):
                        if s[mid] == "+" and x + y <= 1000:
                            ans.add(x + y)
                        elif s[mid] == "*" and x * y <= 1000:
                            ans.add(x * y)
            return ans

        cand = fn(0, len(s))
        ans = 0
        for x in answers:
            if x == target:
                ans += 5
            elif x in cand:
                ans += 2
        return ans
