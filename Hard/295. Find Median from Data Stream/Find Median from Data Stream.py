#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find Median from Data Stream
@time: 2019/8/29 15:54
"""

import bisect


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)

    def findMedian(self) -> float:
        l = len(self.arr)
        if l % 2 == 0:
            return (self.arr[l // 2 - 1] + self.arr[l // 2]) / 2
        else:
            return self.arr[l // 2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
