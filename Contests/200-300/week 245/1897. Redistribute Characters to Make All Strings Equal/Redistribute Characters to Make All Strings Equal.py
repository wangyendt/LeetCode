#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Redistribute Characters to Make All Strings Equal
@time: 2021/06/13 17:01
"""

from typing import *
import collections


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        cnt = collections.Counter(''.join(words))
        for k, v in cnt.items():
            if v % n != 0:
                return False
        return True
