# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Painting a Grid With Three Different Colors.py
@time: 2021/07/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

import itertools
import functools


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7

        def check(pos):
            return all(a != b for a, b in zip(pos, pos[1:]))

        def neighs(pos1, pos2):
            return all(a != b for a, b in zip(pos1, pos2))

        states = {''.join(pos) for pos in itertools.product('RGB', repeat=m) if check(pos)}
        adj = {}
        for state in states:
            adj[state] = [next_state for next_state in states if neighs(state, next_state)]

        @functools.lru_cache(None)
        def f(prv_state, N):
            if N == 0:
                return 1
            return sum(f(next_state, N - 1) for next_state in adj[prv_state]) % mod

        return sum(f(state, n - 1) for state in states) % mod
