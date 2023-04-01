# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Unique Length-3 Palindromic Subsequences.py
@time: 2021/07/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

import string


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in string.ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                res += len(set(s[i + 1: j]))
        return res
