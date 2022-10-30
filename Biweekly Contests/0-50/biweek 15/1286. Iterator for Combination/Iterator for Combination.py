#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Iterator for Combination
@time: 2019/12/16 15:19
"""

import itertools


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combs = list(itertools.combinations(characters, combinationLength))
        self.cnt = 0
        self.amount = len(self.combs)

    def next(self) -> str:
        self.cnt += 1
        return ''.join(self.combs[self.cnt - 1])

    def hasNext(self) -> bool:
        if self.cnt == self.amount:
            return False
        return True


# Your CombinationIterator object will be instantiated and called as such:
iterator = CombinationIterator('abc', 2)
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
