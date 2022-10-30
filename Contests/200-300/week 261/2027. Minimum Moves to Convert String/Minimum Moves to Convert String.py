# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Minimum Moves to Convert String.py
@time: 2021/10/04
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""


class Solution:
    def minimumMoves(self, s: str) -> int:
        p = 0
        n = len(s)
        ret = 0
        while p < n:
            t = s[p]
            if t == 'X':
                ret += 1
                p += 3
            else:
                p += 1
        return ret
