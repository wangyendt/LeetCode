#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Fancy Sequence
@time: 2020/10/18 23:39
"""


class Fancy:

    def __init__(self):
        self.A = []
        self.add = [0]
        self.mul = [1]

    def append(self, a):
        self.A.append(a)
        self.add.append(self.add[-1])
        self.mul.append(self.mul[-1])

    def addAll(self, inc):
        self.add[-1] += inc

    def multAll(self, m):
        self.add[-1] *= m
        self.mul[-1] *= m

    def getIndex(self, i):
        if i >= len(self.A): return -1
        m = self.mul[-1] // self.mul[i]
        inc = self.add[-1] - self.add[i] * m
        return (self.A[i] * m + inc) % (10 ** 9 + 7)

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
