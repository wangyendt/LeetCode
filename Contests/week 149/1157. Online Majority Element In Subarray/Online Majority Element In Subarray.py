#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Online Majority Element In Subarray
@time: 2019/8/20 14:16
"""

import bisect
import collections
import random


class MajorityChecker:

    def __init__(self, A):
        a2i = collections.defaultdict(list)
        for i, x in enumerate(A):
            a2i[x].append(i)
        self.A, self.a2i = A, a2i

    def query(self, left, right, threshold):
        for _ in range(10):
            a = self.A[random.randint(left, right)]
            l = bisect.bisect_left(self.a2i[a], left)
            r = bisect.bisect_right(self.a2i[a], right)
            if r - l >= threshold:
                return a
        return -1


class MajorityChecker2:

    def __init__(self, arr: list):
        self.cnter = []
        for ai, a in enumerate(arr):
            self.cnter.append(collections.Counter(arr[:ai + 1]))

    def query(self, left: int, right: int, threshold: int) -> int:
        cnter = self.cnter[right] + collections.Counter()
        if left > 0:
            cnter -= self.cnter[left - 1]
        res = cnter.most_common(1)
        if res and res[0][1] >= threshold:
            return res[0][0]
        else:
            return -1


# arr = [1, 1, 2, 2, 1, 1]
# obj = MajorityChecker(arr)
# param_1 = obj.query(0, 5, 4)
# param_2 = obj.query(0, 3, 3)
# param_3 = obj.query(2, 3, 2)
arr = [2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2]
obj = MajorityChecker(arr)
print(obj.query(2, 9, 7))
print(obj.query(9, 11, 2))
print(obj.query(2, 11, 7))
print(obj.query(3, 4, 2))
print(obj.query(0, 1, 2))
print(obj.query(6, 9, 3))
print(obj.query(3, 12, 7))
print(obj.query(3, 10, 6))
print(obj.query(7, 11, 4))
print(obj.query(0, 6, 4))
