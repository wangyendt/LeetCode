#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: 2
@time: 2021/04/03 22:28
"""


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        res1 = sentence1.split(' ')
        res2 = sentence2.split(' ')
        if len(res1) == len(res2):
            return all(r1 == r2 for r1, r2 in zip(res1, res2))
        if len(res1) > len(res2):
            res1, res2 = res2, res1
        while res1:
            if res1[0] == res2[0]:
                res1.pop(0)
                res2.pop(0)
            else:
                break
        while res1:
            if res1[-1] == res2[-1]:
                res1.pop()
                res2.pop()
            else:
                break
        return len(res1) == 0
