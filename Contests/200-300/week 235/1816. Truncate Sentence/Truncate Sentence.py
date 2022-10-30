#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Truncate Sentence
@time: 2021/04/04 10:31
"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split(' ')[:k])
