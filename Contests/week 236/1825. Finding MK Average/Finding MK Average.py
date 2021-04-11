#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Finding MK Average.py 
@time: 2021/04/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import sys

sys.path.append('..')
from Tools.API_utils import *
import collections
from sortedcontainers import SortedList


class MKAverage:
    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.deque = collections.deque()
        self.sl = SortedList()
        self.total = self.first_k = self.last_k = 0

    def addElement(self, num: int) -> None:
        self.total += num
        self.deque.append(num)
        index = self.sl.bisect_left(num)
        if index < self.k:
            self.first_k += num
            if len(self.sl) >= self.k:
                self.first_k -= self.sl[self.k - 1]
        if index >= len(self.sl) + 1 - self.k:
            self.last_k += num
            if len(self.sl) >= self.k:
                self.last_k -= self.sl[-self.k]
        self.sl.add(num)
        if len(self.deque) > self.m:
            num = self.deque.popleft()
            self.total -= num
            index = self.sl.index(num)
            if index < self.k:
                self.first_k -= num
                self.first_k += self.sl[self.k]
            elif index >= len(self.sl) - self.k:
                self.last_k -= num
                self.last_k += self.sl[-self.k - 1]
            self.sl.remove(num)

    def calculateMKAverage(self) -> int:
        if len(self.sl) < self.m:
            return -1
        return (self.total - self.first_k - self.last_k) // (self.m - 2 * self.k)


class Fenwick:

    def __init__(self, n: int):
        self.nums = [0] * (n + 1)

    def sum(self, k: int) -> int:
        k += 1
        ans = 0
        while k:
            ans += self.nums[k]
            k &= k - 1  # unset last set bit
        return ans

    def add(self, k: int, x: int) -> None:
        k += 1
        while k < len(self.nums):
            self.nums[k] += x
            k += k & -k


class MKAverage2:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.data = collections.deque()
        self.value = Fenwick(10 ** 5 + 1)
        self.index = Fenwick(10 ** 5 + 1)

    def addElement(self, num: int) -> None:
        self.data.append(num)
        self.value.add(num, num)
        self.index.add(num, 1)
        if len(self.data) > self.m:
            num = self.data.popleft()
            self.value.add(num, -num)
            self.index.add(num, -1)

    def _getindex(self, k):
        lo, hi = 0, 10 ** 5 + 1
        while lo < hi:
            mid = lo + hi >> 1
            if self.index.sum(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def calculateMKAverage(self) -> int:
        if len(self.data) < self.m: return -1
        lo = self._getindex(self.k)
        hi = self._getindex(self.m - self.k)
        ans = self.value.sum(hi) - self.value.sum(lo)
        ans += (self.index.sum(lo) - self.k) * lo
        ans -= (self.index.sum(hi) - (self.m - self.k)) * hi
        return ans // (self.m - 2 * self.k)


call_me(
    MKAverage,
    ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement",
     "addElement", "addElement", "calculateMKAverage"], [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
)
