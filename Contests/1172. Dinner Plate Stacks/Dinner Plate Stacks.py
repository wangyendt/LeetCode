# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/26 16:45
# software: PyCharm


import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = [[]]
        self.capacity = capacity
        self.q = []

    def push(self, val: int) -> None:
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        if not self.q:
            self.stacks[-1].append(val)
            return
        i = heapq.heappop(self.q)
        if i < len(self.stacks):
            self.stacks[i].append(val)

    def pop(self) -> int:
        res = -1
        if not self.stacks: return res
        if len(self.stacks[-1]) == 1:
            res = self.stacks.pop()[0]
        else:
            res = self.stacks[-1].pop()
        return res

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks): return -1
        if not self.stacks[index]: return -1
        res = self.stacks[index].pop()
        heapq.heappush(self.q, index)
        return res

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
