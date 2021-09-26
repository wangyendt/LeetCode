# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Grid Game.py
@time: 2021/09/26
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        A1, A2 = grid[0], grid[1]
        psum1, psum2 = [0] * (n + 1), [0] * (n + 1)
        for i in range(n)[::-1]:
            psum1[i] = psum1[i + 1] + A1[i]
        for i in range(n):
            psum2[i + 1] = psum2[i] + A2[i]
        ret = 1e10
        for i in range(n):
            ret = min(ret, max(psum1[i + 1], psum2[i]))
        return ret
