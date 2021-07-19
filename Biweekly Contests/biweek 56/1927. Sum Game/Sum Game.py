# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Sum Game.py
@time: 2021/07/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""


class Solution:
    def sumGame(self, num: str) -> bool:
        half, bal, q = len(num) // 2, 0, 0
        for i in range(half):
            c, d = num[i], num[i + half]
            if c == '?':
                q -= 1
            else:
                bal += int(c)
            if d == '?':
                q += 1
            else:
                bal -= int(d)
        return bal * 2 != q * 9
