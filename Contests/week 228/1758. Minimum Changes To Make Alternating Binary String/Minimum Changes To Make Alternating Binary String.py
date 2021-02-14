# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Minimum Changes To Make Alternating Binary String.py
@time: 2021/02/14
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""


class Solution:
    def minOperations(self, s: str) -> int:
        def helper(a, b, t):
            res = 0
            for i in range(len(t)):
                if i % 2 == 0 and t[i] == b:
                    res += 1
                if i % 2 == 1 and t[i] == a:
                    res += 1
            return res

        return min(helper('0', '1', s), helper('1', '0', s))
