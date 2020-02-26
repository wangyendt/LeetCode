#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Product of the Last K Numbers
@time: 2020/2/26 14:27
"""


class ProductOfNumbers:

    def __init__(self):
        self.A = [1]

    def add(self, a):
        if a == 0:
            self.A = [1]
        else:
            self.A.append(self.A[-1] * a)

    def getProduct(self, k):
        if k >= len(self.A): return 0
        return self.A[-1] // self.A[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
