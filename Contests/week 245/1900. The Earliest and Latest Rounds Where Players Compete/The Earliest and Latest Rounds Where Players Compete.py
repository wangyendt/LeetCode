#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: The Earliest and Latest Rounds Where Players Compete
@time: 2021/06/13 23:31
"""

from functools import lru_cache
from typing import *


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache
        def dp(l, r, m):
            # make sure l <= r
            if l > r:
                return dp(r, l, m)
            # base case
            if l == r:
                return 1, 1
            # dp transition
            nxt_m = (m + 1) // 2
            ans = [n, 0]
            for i in range(1, l + 1):
                l_win, l_lose = i - 1, l - i
                for j in range(max(r - (m // 2) - 1, 0) + l_lose + 1, min(r - 1 - l_win, nxt_m - i) + 1):
                    tmp = dp(i, j, nxt_m)
                    ans = min(ans[0], tmp[0]), max(ans[1], tmp[1])
            return ans[0] + 1, ans[1] + 1

        return dp(firstPlayer, n - secondPlayer + 1, n)
