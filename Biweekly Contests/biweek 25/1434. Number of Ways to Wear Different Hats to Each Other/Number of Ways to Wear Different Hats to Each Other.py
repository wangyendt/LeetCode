#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/9 17:04
@Author:  wang121ye
@File: Number of Ways to Wear Different Hats to Each Other.py
@Software: PyCharm
"""

from functools import lru_cache


class Solution:
    def numberWays(self, hats: list(list())) -> int:
        ppl = dict()  # mapping : hat -> people
        for i, hat in enumerate(hats):
            for x in hat: ppl.setdefault(x, []).append(i)

        @lru_cache(None)
        def fn(h, mask):
            """Return the number of ways to wear h to last hats among people whose
            availability is indicated by mask"""
            if mask == (1 << len(hats)) - 1: return 1  # # set bits = # people
            if h == 40: return 0  # if used all hat,
            ans = fn(h + 1, mask)
            for p in ppl.get(h + 1, []):  # loop through all people preferring the hat
                if mask & (1 << p): continue  # if taken, continue
                mask |= 1 << p  # set bit
                ans += fn(h + 1, mask)
                mask ^= 1 << p  # reset bit
            return ans % 1000000007

        return fn(0, 0)
