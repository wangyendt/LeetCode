# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Maximum Number of Words You Can Type.py
@time: 2021/07/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ret = 0
        for t in text.split(' '):
            if not any(tt in brokenLetters for tt in t):
                ret += 1
        return ret
