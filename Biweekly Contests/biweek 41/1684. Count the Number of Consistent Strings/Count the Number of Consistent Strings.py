#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count the Number of Consistent Strings
@time: 2020/12/12 22:30
"""

from typing import *


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ret = 0
        allowed = set(allowed)
        for word in words:
            if all(w in allowed for w in set(word)):
                ret += 1
        return ret
