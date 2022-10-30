#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Design Front Middle Back Queue
@time: 2020/11/29 00:08
"""


class FrontMiddleBackQueue:

    def __init__(self):
        self.buffer = []

    def pushFront(self, val: int) -> None:
        self.buffer[0:0] = [val]

    def pushMiddle(self, val: int) -> None:
        n = len(self.buffer)
        self.buffer[n // 2:n // 2] = [val]

    def pushBack(self, val: int) -> None:
        self.buffer.append(val)

    def popFront(self) -> int:
        # print(self.buffer)
        if not self.buffer: return -1
        ret = self.buffer[0]
        self.buffer[0:1] = []
        return ret

    def popMiddle(self) -> int:
        # print(self.buffer)
        if not self.buffer: return -1
        n = len(self.buffer)
        ret = self.buffer[(n - 1) // 2]
        self.buffer[(n - 1) // 2:(n - 1) // 2 + 1] = []
        return ret

    def popBack(self) -> int:
        print(self.buffer)
        if not self.buffer: return -1
        return self.buffer.pop()

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
